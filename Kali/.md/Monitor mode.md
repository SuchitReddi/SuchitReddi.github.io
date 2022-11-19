[Back](..)

There are two ways to enable monitor mode for wlan

USING IFCONFIG AND IWCONFIG\
iwconfig to check mode of wlan0\
ifconfig wlan0 down to disable wireless interface\
airmon-ng check kill to kill processes which can interfere with it\
iwconfig wlan0 mode monitor to change to monitor mode\
ifconfig wlan0 up to enable wireless interface again\

USING AIRMON-NG\
ifconfig wlan0 down\
airmon-ng check kill\
airmon-ng start wlan0\ 
ifconfig wlan0 up

[Back](..)