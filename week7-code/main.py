from lib import ModemController, HTTP, MQTT, ATCOM
import time


def main():
    http_url = "https://webhook.site/30ef4a9e-2b82-4a36-bb1a-3b20fff521ae"
    post_message = "Message=Hello Quectel"
    mqtt_url = "broker.hivemq.com"
    mqtt_message = "This is test data, hello MQTT."

    modem = ModemController()
    at = ATCOM(modem)
    mq = MQTT(at)
    http = HTTP(at)
    # protocol = PROTOCOL(at)
    if modem.available_port():
        modem.open_connection()

        # PPP/QMI
        # response = at.send_at_com("AT+QCFG=\"usbnet\"")
        # response = at.send_at_com("AT+QCFG=\"usbnet\",0")
        # response = at.send_at_com("AT+CFUN=1,1")

        # ECM
        # response = at.send_at_com("AT+CGDCONT=1,\"IPV4V6\",\"de1.super\"")
        # response = at.send_at_com("AT+QCFG=\"usbnet\",1")
        # response = at.send_at_com("AT+CFUN=1,1")

        print(response)
        # http.http_get(http_url)
        # http.http_post(http_url, post_message)
        # mq.send_mqtt(mqtt_url, mqtt_message)
        modem.close_connection()
    else:
        print("Error: Modem port not find")


main()

"""
+CGDCONT: 1,"IPV4V6","de1.super","0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0",0,0,0,0
+CGDCONT: 2,"IPV4V6","ims","0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0",0,0,0,0
+CGDCONT: 3,"IPV4V6","SOS","0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0",0,0,0,1
"""