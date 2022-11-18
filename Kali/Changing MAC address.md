We can see MAC address by using ifconfig
MAC address looks like,ether 00:00:27:59:1b:54 
IP address looks like inet 10.20.54.335

To change MAC, first we have to disable that interface
ifconfig wlan0 down to disable wireless adapter interface.
ifconfig wlan0 hw ether 00:11:22:33:44:55 will change MAC.
ifconfig wlan0 up will enable interface again.

We used hw because we want to change hardware address.
An important thing to notice is that MAC address will 
revert to original after restarting device.
