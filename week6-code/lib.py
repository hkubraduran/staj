import serial
import time 
from serial.tools import list_ports

class ModemController:
	def __init__(self, port=None, baudrate=115200, parity=serial.PARITY_NONE, timeout=1):
		self.port=port
		self.baudrate=baudrate
		self.parity=parity
		self.timeout=timeout
		self.serial_connection=None
		
	def available_port(self):
		if self.port and self.test_connection(self.port):
			print(f"The port is already available.")
			return True
		ports=list_ports.comports()
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
	
	def send_at_com(self, com):
		if self.serial_connection:
			try:
				self.serial_connection.write((com + "\r\n").encode())	
				time.sleep(3)
				response = self.serial_connection.read_all().decode()
				return response
			except serial.SerialException as e:
				print(f"Error: AT command not send. - {e}")
		else:
			print("Error: There is no connection!")
	url = "https://webhook.site/2e30d8cc-cd7f-48bf-8951-ce0a08469207"
	#url = "https://www.alipay.com"
	url_bytes = len(url.encode('utf-8'))
	#print(url_len)	
  	#57
	get_arr = ["AT+QHTTPCFG=\"contextid\",1",
            "AT+QHTTPCFG=\"responseheader\",1",
            "AT+QIACT?",
            "AT+CGDCONT=1,\"IPV4V6\",\"de1.super\"",
            "AT+QICSGP=1,3,\"de1.super\",\"\",\"\",1",
            "AT+QIACT=1",
            f"AT+QHTTPURL={url_bytes},80",
            url,
            "AT+QHTTPGET=80",
            "AT+QHTTPREAD=80",
            ]	

	def http_get(self):
		i = 0
		while i < len(self.get_arr):
			print("HTTP command: ")
			print(self.get_arr[i])
			print("Response: ")
			response = self.send_at_com(self.get_arr[i])

			if i == 2:
				res = response.split('\n')
				#print(res[-2])
				if res[-2].strip() == 'OK':
					#print("inside if block")
					for j in range(0, 3):  # Skip the next 3 commands
						i += 1
						print("Skipping command:", self.get_arr[i])
			# elif i == 6:
			# 	time.sleep(1)

			print(response)
			i += 1
	post_message = "Message=Hello Quectel"
	length = len(post_message.encode('utf-8'))
	post_arr = [
		"AT+QHTTPCFG=\"contextid\",1",
		"AT+QHTTPCFG=\"responseheader\",1",
        "AT+QIACT?",
        "AT+CGDCONT=1,\"IPV4V6\",\"de1.super\"",
        "AT+QICSGP=1,3,\"de1.super\",\"\",\"\",1",
        "AT+QIACT=1",
        f"AT+QHTTPURL={url_bytes},80",
        url,
        f"AT+QHTTPPOST={length},80,80",
        post_message,
        "AT+QHTTPREAD=80",
	]

	def http_post(self):
		i = 0
		while i < len(self.post_arr):
			print("HTTP command: ")
			print(self.post_arr[i])
			print("Response: ")
			response = self.send_at_com(self.post_arr[i])

			if i == 2:
				res = response.split('\n')
				#print(res[-2])
				if res[-2].strip() == 'OK':
					#print("inside if block")
					for j in range(0, 3):  # Skip the next 3 commands
						i += 1
						print("Skipping command:", self.post_arr[i])
			# elif i == 7:
			# 	time.sleep(3)
			
			print(response)
			i += 1
	
	mqtt_arr = [
		"AT+QMTOPEN=0, \"broker.hivemq.com\", 1883",
		"AT+QMTOPEN?",
		"AT+QMTCONN=0, \"clientExample\"",
		"AT+QMTSUB=0, 1, \"topic/pub\", 0",
		"AT+QMTPUBEX=0, 0, 0, 0, \"topic/pub\", 30",
		"This is test data, hello MQTT.",
		"AT+QMTSUB=0, 1, \"topic/pub\", 0",
		"AT+QMTDISC=0"
	]

	def send_mqtt(self):
		i = 0
		while i < len(self.mqtt_arr):
      
			print("Command: ")
			print(self.mqtt_arr[i])
			response = self.send_at_com(self.mqtt_arr[i])
   
			print(response)
			i += 1