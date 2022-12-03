[Back](..)

During recent kali installation of kali 22.2 and kali kernel of 5.16.0-kali7-amd64, I experienced problems at installing grub bootloader with the exact message "grub install dummy failed"\
I solved this error by going to uefi settings, enabling safe boot and clearing safe boot keys.\
After that, grub installed successfully but I observed no ethernet and wifi if installed without connecting to ethernet, but after connecting to ethernet, there was no wifi. I installed only gnome and I got both wifi and ethernet.

[Back](..)