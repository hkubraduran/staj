# 1.HAFTA RAPORU

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

### Raspberry Pi 3B+ Kurulumu
* I started by installing the operating system on the SD card.	
* [Raspberry Pi OS Images](https://www.raspberrypi.com/software/operating-systems/ ) 
I downloaded the raspberryi pi 3b+ image file from the page and transferred it to the sd card with Balena Etcher.
* Then I connected my sd card and other necessary hardware (mouse, keyboard, screen, lan cable, power cable) to the raspberry pi.
* Finally, I completed the raspberry pi installation from the pop-up screen.
### Sixfab 4G/LTE Cellular Modem Kurulumu
* ]I used sixfab [document](https://docs.sixfab.com/docs/raspberry-pi-4g-lte-cellular-modem-kit-getting-started) for modem installation.(https://docs.sixfab.com/docs/raspberry-pi-4g-lte-cellular-modem-kit-getting-started) yararlandım. 
* Dökümandaki adımları takip ederek donanımları birleştirdim.
* Daha sonra [sixfab core device bağlantısını](https://connect.sixfab.com/) yaptım.
* sudo bash -c "$(curl -sN https://install.connect.sixfab.com)" -- -t YOUR_TOKEN_APPEARS_HERE' -d kodunu terminalde çalıştırıp bağlantıyı tamamlamış oldum.


<!--stackedit_data:
eyJoaXN0b3J5IjpbOTI5NDQ3NDIsLTg5OTU4OTIzNF19
-->