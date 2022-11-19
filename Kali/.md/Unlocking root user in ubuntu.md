[Back](..)

Use sudo -i passwd root\
But, ubuntu has an additional security layer to block root account login.\
We should change some files, but take backups of them for any future problems.

mkdir backup\
then cp /etc/gdm3/custom.conf backup/\
then cp /etc/pam.d/gdm-password backup/\
Check using ls backup/\
if there are custom.conf and gdm-password in backup, it is a success

Now, use sudo nano /etc/gdm3/custom.conf\
Type AllowRoot=true between [security] and [xdmcp]\
Save it using ^o and enter then ^x\
sudo nano /etc/pam.d/gdm-password\
Here, put # in the third line before auth required pam_succeed_if.so user !=root quiet_success to make it as a comment, and save it.\
Now, reboot using sudo reboot -f

To disable root password and lock it again, use sudo passwd -dl root\
Then, restore original backup files of custom.conf and gdm-password\
sudo cp backup/gdm-password /etc/pam.d/gdm-password\
sudo cp backup/custom.conf /etc/gdm3/custom.conf\
Or, remove AllowRoot=true form custom.conf and # form gdm-password\
Refer to 
https://www.computernetworkingnotes.com/linux-tutorials/how-to-enable-and-disable-root-login-in-ubuntu.html#:~:text=Enabling%20and%20disable%20root%20login%20in%20nutshell&text=CLI%20%26%20GUI%20both-,Use%20the%20sudo%20%E2%80%93i%20passwd%20root%20command.,conf%20file.

[Back](..)