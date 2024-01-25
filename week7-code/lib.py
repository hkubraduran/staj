import serial
import time
from serial.tools import list_ports


class ModemController:
    def __init__(self, port=None, baudrate=115200, parity=serial.PARITY_NONE, timeout=1):
        self.port = port
        self.baudrate = baudrate
        self.parity = parity
        self.timeout = timeout
        self.serial_connection = None

    def available_port(self):
        if self.port and self.test_connection(self.port):
            print(f"The port is already available.")
            return True
        ports = list_ports.comports()
        for i in ports:
            if self.test_connection(i.device):
                self.port = i.device
                print(f"Modem port is find: {self.port}")
                return self.port
        print(f"Error: Modem port is not found!")
        return False

    def test_connection(self, port):
        try:
            serial_connection = serial.Serial(port=port,
                                              baudrate=self.baudrate,
                                              parity=self.parity,
                                              timeout=self.timeout)
            serial_connection.write(b'AT\r\n')
            time.sleep(1)
            response = serial_connection.read_all().decode()
            serial_connection.close()
            return "OK" in response
        except serial.SerialException as e:
            print(f"Error: Modem connection could not be tested - {e}")
            return False

    def open_connection(self):
        if not self.port and not self.available_port():
            return
        try:
            self.serial_connection = serial.Serial(port=self.port,
                                                   baudrate=self.baudrate,
                                                   parity=self.parity,
                                                   timeout=self.timeout)
            print(f"Modem connection is done: {self.serial_connection.name}")
        except serial.SerialException as e:
            print(f"Modem connection is failed. - {e}")

    def close_connection(self):
        if self.serial_connection:
            self.serial_connection.close()
            print("Modem connection closed.")


class ATCOM:
    def __init__(self, modem):
        self.modem = modem

    def send_at_com(self, com):
        if self.modem.serial_connection:
            try:
                self.modem.serial_connection.write((com + "\r\n").encode())
                time.sleep(3)
                response = self.modem.serial_connection.read_all().decode()
                return response
            except serial.SerialException as e:
                print(f"Error: AT command not send. - {e}")
        else:
            print("Error: There is no connection!")


class HTTP:

    def __init__(self, atcom):
        self.atcom = atcom

    def pdp_connect(self):
        pdp_arr = ["AT+QHTTPCFG=\"contextid\",1",
                   "AT+QHTTPCFG=\"responseheader\",1",
                   "AT+QIACT?",
                   "AT+CGDCONT=1,\"IPV4V6\",\"de1.super\"",
                   "AT+QICSGP=1,3,\"de1.super\",\"\",\"\",1",
                   "AT+QIACT=1"
                   ]
        i = 0
        while i < len(pdp_arr):
            print(f"Command:\n{pdp_arr[i]}")
            print("Response:")
            response = self.atcom.send_at_com(pdp_arr[i])
            print(response)
            if i == 2:
                res = response.split('\n')
                # print(res[-2])
                if res[-2].strip() == 'OK':
                    # print("inside if block")
                    for j in range(0, 3):  # Skip the next 3 commands
                        i += 1
                        print("Skipping command:", pdp_arr[i])
            # elif i == 6:

            i += 1

    def http_get(self, url):
        url_bytes = len(url.encode('utf-8'))
        get_arr = [
            f"AT+QHTTPURL={url_bytes},80",
            url,
            "AT+QHTTPGET=80",
            "AT+QHTTPREAD=80",
        ]
        i = 0
        self.pdp_connect()
        while i < len(get_arr):
            print("HTTP command: ")
            print(get_arr[i])
            print("Response: ")
            response = self.atcom.send_at_com(get_arr[i])

            print(response)
            i += 1

    def http_post(self, url, post_message):
        url_bytes = len(url.encode('utf-8'))
        length = len(post_message.encode('utf-8'))
        post_arr = [
            f"AT+QHTTPURL={url_bytes},80",
            url,
            f"AT+QHTTPPOST={length},80,80",
            post_message,
            "AT+QHTTPREAD=80",
        ]

        i = 0
        self.pdp_connect()
        while i < len(post_arr):
            print("HTTP command: ")
            # print(self.post_arr[i])
            print("Response: ")
            response = self.atcom.send_at_com(post_arr[i])

            print(response)
            i += 1


class MQTT:

    def __init__(self, atcom):
        # self.serial_connection = None

        self.atcom = atcom

    def send_mqtt(self, url, message):
        mqtt_arr = [
            f"AT+QMTOPEN=0, {url}, 1883",
            "AT+QMTOPEN?",
            "AT+QMTCONN=0, \"clientExample\"",
            "AT+QMTSUB=0, 1, \"topic/pub\", 0",
            "AT+QMTPUBEX=0, 0, 0, 0, \"topic/pub\", 30",
            message,
            "AT+QMTSUB=0, 1, \"topic/pub\", 0",
            "AT+QMTDISC=0"
        ]

        i = 0
        while i < len(mqtt_arr):
            print("Command: ")
            # print(self.mqtt_arr[i])
            response = self.atcom.send_at_com(mqtt_arr[i])

            print(response)
            i += 1








