# FINAL REPORT 

## Library

* My library consists of ModemController, ATCOM, HTTP, MQTT classes.
* This library aims to use AT commands to communicate with the modem, to send HTTP requests such as HTTP GET and POST, to connect to a server using the MQTT protocol, to publish on a specific topic and to subscribe that topic. 
* In addition to these, it aims to enable raspberry pi to access the internet by using PPP, ECM, QMI protocols. 

### ModemController Class

* This class contains available_port(), test_connection(), open_connection(), close_connection() functions.
* The "port" parameter is sent to the `test_connection()` function. This function tests whether the port is available and returns "OK" or an error message.
```	def test_connection(self, port):
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
```
* The `available_port()` function sends all ports to the test_connection() function respectively. In this way, all ports are tested and the appropriate port is selected.
```	def available_port(self):
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
```

* The `open_connection()` function opens the connection if the available port is found.
```	def open_connection(self):
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
```
* The `close_connection()` function closes the serial connection if it exists. 
```	def close_connection(self):
		if self.serial_connection:
			self.serial_connection.close()
			print("Modem connection closed.")
```
### ATCOM Class
* This class contains the `send_at_com()` function.
* The "com" parameter is sent to send_at_com(). This parameter is used for the AT commands to be sent.
* In addition, the "modem" object created to use the ModemController class is also defined and used in this class.
* After the AT commands sent, the response is returned.
* The error message, if any, is printed.
```	def send_at_com(self, com):
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
```
### HTTP Class
* This class contains the functions pdp_connect(), http_get(), http_post().

* Inside the pdp_connect() function, I defined the pdp_arr array and added the at commands required for the pdp connection to this array.
* With the while loop, I made sure that all commands in this array are read and the answers are printed.
* I first checked the connection with the `AT+QIACT?` command and according to the answer, if there is a connection, I organized the function to pass the next commands.
    * Passed commands: 
        * `"AT+CGDCONT=1,\"IPV4V6\",\"de1.super\""`
        * `"AT+QICSGP=1,3,\"de1.super\",\"\",\"\",1"`
        * `"AT+QIACT=1"`
```	def pdp_connect(self):
		pdp_arr = ["AT+QHTTPCFG=\"contextid\",1",
			"AT+QHTTPCFG=\"responseheader\",1",
			"AT+QIACT?",
			"AT+CGDCONT=1,\"IPV4V6\",\"de1.super\"",
			"AT+QICSGP=1,3,\"de1.super\",\"\",\"\",1",
			"AT+QIACT=1"
		]
		i= 0
		while i < len(pdp_arr):
			print(f"Command:\n{pdp_arr[i]}")
			print("Response:")
			response = self.atcom.send_at_com(pdp_arr[i])
			print(response)
			if i == 2:
				res = response.split('\n')
				#print(res[-2])
				if res[-2].strip() == 'OK':
					#print("inside if block")
					for j in range(0, 3):  # Skip the next 3 commands
						i += 1
						print("Skipping command:", pdp_arr[i])
			i+=1
```
* The "url" is sent as a parameter to the `http_get()` function.
* I calculated the byte length of this url and used it for the `AT+QHTTPURL` command.
* I added the at commands needed for http get to the get_arr array.
* With the while loop, I took these commands one by one, sent them to the `send_at_com()` function and printed the responses. 
```	def http_get(self, url):
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
```
* The `http_post()` function takes url and post_message as parameters. 
* I calculated the byte length for this URL. 
* I added the commands needed for http post to the post_arr array.
* With the while loop, these commands are sent to the `send_at_com` function respectively. In this way, an http post request is sent. The responses received from the commands are also printed. 
```	def http_post(self, url, post_message):
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
			#print(self.post_arr[i])
			print("Response: ")
			response = self.atcom.send_at_com(post_arr[i])

			print(response)
			i += 1
```
### MQTT Class
* This class contains the send_mqtt() function.
* "url" and "message" are sent as parameters to `send_mqtt()` function.
* I created the mqtt_arr array inside the function and added the AT commands required for mqtt.
* I made sure that these commands are received and sent to the send_at_com function with a while loop and the received responses are printed.
```	def send_mqtt(self, url, message):
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
			#print(self.mqtt_arr[i])
			response = self.atcom.send_at_com(mqtt_arr[i])
   
			print(response)
			i += 1
```
### Main Fonksiyonu 
* Inside this function I added the URls for http and mqtt and the messages to be sent. 
* In order for the classes to be connected to each other, I import the classes and create objects. 
* If the appropriate modem port has been found for proper communication, I have called here the functions to open and close the connection. 
* I also called the HTTP and MQTT functions here. 

