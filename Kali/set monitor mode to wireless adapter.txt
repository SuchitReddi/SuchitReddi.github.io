sudo apt update

cd

sudo rmmod r8188eu.ko

git clone https://github.com/aircrack-ng/rtl8188eus.git 

cd

cd rtl8188eus/

sudo -i

echo "blacklist r8188eu.ko" > "/etc/modprobe.d/realtek.conf"

exit

make

sudo make install

sudo modprobe 8188eu

sudo iwconfig

remove and connect wireless adapter if it is not shown
let us assume that it is shown as wlan1 in iwconfig
wlan1 will be shown to be set to managed mode

sudo ip link set wlan1 down

sudo iw dev wlan1 set type monitor

sudo ip link set wlan1 up

sudo iwconfig
 
 you should be able to see wlan1 set to monitor mode now
