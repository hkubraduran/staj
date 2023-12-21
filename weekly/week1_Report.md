# 1.HAFTA RAPORU

### Learning Basic Git Commands and Creating a Github Repository
* First of all, I created a public repository on github. 
* Daha sonra weekly adında bir dizin oluşturdum.
* Masaüstündeki klasörüme README dosyası oluşturdum.
* Daha sonra terminalden sırasıyla aşağıdaki git komutlarını kullanarak README dosyasını github repositorysine ekledim.
	* cd Desktop
	* cd sixfab
	* git init
	* git add README.md
	* git commit -m "README commit"
	* git remote add origin https://github.com/hkubraduran/staj.git
	* git push -u origin master

### Raspberry Pi 3B+ Kurulumu
* Öncelikle işletim sistemini sd karta kurmakla başladım.
	* [Raspberry Pi OS Images](https://www.raspberrypi.com/software/operating-systems/ ) sayfasından raspberryi pi 3b+ image dosyasını indirererek Balena Etcher ile sd karta aktardım.
* Daha sonra sd kartımı ve diğer gerekli donanımları(mouse,klavye,ekran,lan kablosu,güç kablosu) raspberry pi'a bağladım.
* Son olarak raspberry pi kurulumunu açılan ekrandan tamamladım.
### Sixfab 4G/LTE Cellular Modem Kurulumu
* Modem kurulumu için sixfab [dökümanından](https://docs.sixfab.com/docs/raspberry-pi-4g-lte-cellular-modem-kit-getting-started) yararlandım. 
* Dökümandaki adımları takip ederek donanımları birleştirdim.
* Daha sonra [sixfab core device bağlantısını](https://connect.sixfab.com/) yaptım.
* sudo bash -c "$(curl -sN https://install.connect.sixfab.com)" -- -t YOUR_TOKEN_APPEARS_HERE' -d kodunu terminalde çalıştırıp bağlantıyı tamamlamış oldum.


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTYyMjE1NTkwMCwtODk5NTg5MjM0XX0=
-->