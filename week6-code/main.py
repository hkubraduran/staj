from lib import ModemController
import time
def main():
	modem = ModemController()
	if modem.available_port():
		modem.open_connection()
		
  
		#modem.http_get()
		#modem.http_post()
  
		#response = modem.send_at_com("AT+QMTOPEN?")
  
		# response = modem.send_at_com("AT+QMTOPEN=0, \"broker.hivemq.com\", 1883")
		# print(response)
		# time.sleep(1)
		# response = modem.send_at_com("AT+QMTOPEN?")
		# print(response)
		# response = modem.send_at_com("AT+QMTCONN=0, \"clientExample\"")
		# print(response)
		# response = modem.send_at_com("AT+QMTSUB=0, 1, \"topic/pub\", 0")
		# print(response)
		# response = modem.send_at_com("AT+QMTPUBEX=0, 0, 0, 0, \"topic/pub\", 30")
		# print(response)
		# time.sleep(1)
		# response = modem.send_at_com("This is test data, hello MQTT.")
		# time.sleep(1)
		# print(response)
		# time.sleep(1)
		# response = modem.send_at_com("AT+QMTSUB=0, 1, \"topic/pub\", 0")
		# print(response)
		# response = modem.send_at_com("AT+QMTDISC=0")
		# print(response)
		modem.send_mqtt()
		modem.close_connection()
	else:
		print("Error: Modem port not find")
  
main()
"""
+CGDCONT: 1,"IPV4V6","de1.super","0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0",0,0,0,0
+CGDCONT: 2,"IPV4V6","ims","0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0",0,0,0,0
+CGDCONT: 3,"IPV4V6","SOS","0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0",0,0,0,1
"""