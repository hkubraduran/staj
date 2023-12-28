from lib import ModemController

def main():
	modem = ModemController()
	if modem.available_port():
		modem.open_connection()
		response = modem.send_at_com("AT")
		print(response)
		modem.close_connection()
	else:
		print("Error: Modem port not find")