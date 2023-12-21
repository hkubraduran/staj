## Week 2

### Python Library
* Research about python library that will be created to communicate with the modem
	* I got information about serial communication using this [site](https://devtut.github.io/python/python-serial-communication-pyserial.html#initialize-serial-device) 
* AT Commands 
	* `ls /dev/tty*` 
		* It shows all USB devices that plugged into the raspberry pi
		* I learned "/dev/ttyUSB0  /dev/ttyUSB1 /dev/ttyUSB2 /dev/ttyUSB3" these are my cellular modem.
	* `sudo apt install python3-pip`
	* `pip3 install atcom`
	* `atcom AT` 
		* This command selects the appropriate port
* Protocols
	* They are used for the internet connection
		* I learned that these are the commonly used protocols for Internet connection are PPP, QMI and ECM.
	
### Wifi Configuration on Raspberry Pi
* I used [raspberry pi imager](https://www.raspberrypi.com/software/) for wifi connection 
*I used a [video](https://www.youtube.com/watch?v=nZyyfJYOhbM) named "Setup Raspberry PI OS with SSH and WIFI"
* I activated ssh in raspberry pi configuration 
	*  raspberryi pi preferences --> interfaces --> SSH enable 
* Then, I connected raspberry pi to internet with `ssh kubra@IP address of raspberry pi` command


### Remote Connection with VNC 
* I downloaded [VNC client](https://www.realvnc.com/en/connect/download/viewer/) on my computer to have remote access to the Raspberry pi.
* For VNC, two devices must be connected to the same wifi.
*  I also opened VNC on the Raspberry pi.
	* raspberryi pi preferences --> interfaces --> VNC enable 
* I connected raspberry pi to monitor and learned the IP  adress with `ifconfig` command (firstly you need to unplug the modem, and then connect the same wifi with the laptop).
* I opened VNC Viewer from my own computer, typed IP address and connected to raspberyy pi.

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyNzcxODY3NDJdfQ==
-->