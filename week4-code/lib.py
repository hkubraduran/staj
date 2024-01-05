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
				time.sleep(5)
				response = self.serial_connection.read_all().decode()
				return response
			except serial.SerialException as e:
				print(f"Error: AT command not send. - {e}")
		else:
			print("Error: There is no connection!")
		
