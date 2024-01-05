from lib import ModemController

def main():
	modem = ModemController()
	if modem.available_port():
		modem.open_connection()
        #modem.send_at_com("AT+CGDCONT?")
		#modem.send_at_com("AT+QICSGP=1,3,\"de1.super\",\"\",\"\",1")
	
		#response = modem.send_at_com("AT+CGATT?")
		#response = modem.send_at_com("AT+CGREG?")
		#modem.send_at_com("AT+QIACT=1")
		#response = modem.send_at_com("AT+QIACT?")
		#response = modem.send_at_com("AT+QHTTPCFG=\"responseheader\",1")
		#response = modem.send_at_com("AT+QHTTPCFG=\"sslctxid\",1")
		#response = modem.send_at_com("AT+QSSLCFG=\"sslversion\",1,1")
		#response = modem.send_at_com("AT+QSSLCFG=\"ciphersuite\",1,0x0005")
		#response = modem.send_at_com("AT+QSSLCFG=\"seclevel\",1,0")
		#response = modem.send_at_com(f"AT+QHTTPURL={url_bytes},80")
		#print(response)
		#time.sleep(3)
		#response = modem.send_at_com(url)
		#print(response)
		#time.sleep(3)
		#response = modem.send_at_com("AT+QHTTPGET=80")
		#response = modem.send_at_com("AT+CPIN?")
		response = modem.send_at_com("AT")
		print(response)
		modem.close_connection()
	else:
		print("Error: Modem port not find")
"""
+CGDCONT: 1,"IPV4V6","de1.super","0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0",0,0,0,0
+CGDCONT: 2,"IPV4V6","ims","0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0",0,0,0,0
+CGDCONT: 3,"IPV4V6","SOS","0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0",0,0,0,1
"""