from lib import ModemController
import time
def main():
	modem = ModemController()
	if modem.available_port():
		modem.open_connection()
		
  
		#modem.http_get()
		modem.http_post()
		modem.close_connection()
	else:
		print("Error: Modem port not find")
  
main()
"""
+CGDCONT: 1,"IPV4V6","de1.super","0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0",0,0,0,0
+CGDCONT: 2,"IPV4V6","ims","0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0",0,0,0,0
+CGDCONT: 3,"IPV4V6","SOS","0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0",0,0,0,1
"""