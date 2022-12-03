[Back](..)

Grub bootloader generally has other OSs on the device in it.\
But the latest grub version removed that option by default. We should enable it ourself.\ 

nano /etc/default/grub

add GRUB_DISABLE_OS_PROBER=false\
edit the default with the number for os starting from 0 for kali\
change timeout\
then ^O and enter\
then ^X to exit\
finally type update-grub

[Back](..)