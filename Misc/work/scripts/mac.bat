@echo off
set file_path=C:\Program Files\Oracle\VirtualBox\
cd /d %file_path%

echo The default path is %file_path%.
echo.
set /p file_path="If you want to change the path, give the absolute path here, or just type a dot (.): "
cd /d %file_path%
echo.

VBoxManage.exe modifyvm "monterey" --cpuidset 00000001 000106e5 00100800 0098e3fd bfebfbff
VBoxManage.exe setextradata "monterey" "VBoxInternal/Devices/efi/0/Config/DmiSystemProduct" "iMac19,1"
VBoxManage.exe setextradata "monterey" "VBoxInternal/Devices/efi/0/Config/DmiSystemVersion" "1.0"
VBoxManage.exe setextradata "monterey" "VBoxInternal/Devices/efi/0/Config/DmiBoardProduct" "Mac-AA95B1DDAB278B95"
VBoxManage.exe setextradata "monterey" "VBoxInternal/Devices/smc/0/Config/DeviceKey" "ourhardworkbythesewordsguardedpleasedontsteal(c)AppleComputerInc"
VBoxManage.exe setextradata "monterey" "VBoxInternal/Devices/smc/0/Config/GetKeyFromRealSMC" 1
VBoxManage.exe setextradata "monterey" "VBoxInternal/TM/TSCMode" "RealTSCOffset"
pause