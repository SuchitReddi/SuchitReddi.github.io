AIRGEDDON

go to browser and go to airgeddon github
click on green button for code and copy the https address which looks like
https://github.com/v1s1t0r1sh3r3/airgeddon.git
go to terminal and then type git clone <copied link>

to use it, type cd airgeddon
then ./airgeddon.sh

BRAVE

go to browser and search brave for linux or use these codes
sudo apt install apt-transport-https curl

sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list

sudo apt update

sudo apt install brave-browser

VLC MEDIA PLAYER

use sudo apt install vlc

VIRTUAL BOX
sudo apt update
sudo apt full-upgrade -y
[ -f /var/run/reboot-required ] && sudo reboot -f

kali@kali:~$ wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- \
  | gpg --dearmor \
  | sudo tee /usr/share/keyrings/virtualbox-archive-keyring.gpg
  
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/virtualbox-archive-keyring.gpg] http://download.virtualbox.org/virtualbox/debian buster contrib" \
  | sudo tee /etc/apt/sources.list.d/virtualbox.list
  
sudo apt update
sudo apt install -y dkms
sudo apt install -y virtualbox virtualbox-ext-pack
virtualbox
