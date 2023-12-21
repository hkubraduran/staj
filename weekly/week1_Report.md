# Week 1- Report

### Learning Basic Git Commands and Creating a Github Repository
* First of all, I created a public repository on github. 
* Then I created a directory called weekly.
* I created a README file in my folder on the desktop.
* Then I added the README file to the github repository using the following git commands respectively from the terminal.
	* cd Desktop
	* cd sixfab
	* git init
	* git add README.md
	* git commit -m "README commit"
	* git remote add origin https://github.com/hkubraduran/staj.git
	* git push -u origin master

### Raspberry Pi 3B+ Installation
* I started by installing the operating system on the SD card.	
* [Raspberry Pi OS Images](https://www.raspberrypi.com/software/operating-systems/ ) 
I downloaded the raspberryi pi 3b+ image file from the page and transferred it to the sd card with Balena Etcher.
* Then I connected my sd card and other necessary hardware (mouse, keyboard, screen, lan cable, power cable) to the raspberry pi.
* Finally, I completed the raspberry pi installation from the pop-up screen.
### Sixfab 4G/LTE Cellular Modem Setup
* I used sixfab [document](https://docs.sixfab.com/docs/raspberry-pi-4g-lte-cellular-modem-kit-getting-started) for modem installation.
* I combined the hardware following the steps in the document.
* Then I made [sixfab core device connection](https://connect.sixfab.com/).
* sudo bash -c "$(curl -sN https://install.connect.sixfab.com)" -- -t YOUR_TOKEN_APPEARS_HERE' -d 
I ran the code above  in the terminal and completed the connection.


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0NjM4Njg4NjQsLTg5OTU4OTIzNF19
-->