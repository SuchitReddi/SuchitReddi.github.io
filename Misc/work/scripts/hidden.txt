@echo off
setlocal
echo Hiding...
echo.

REM Setting the window size to very small (Note: If the columns is less than 15, it isn't working)
mode con lines=1 cols=15

REM The registry command to hide hidden files is below, you need to change the 0 after /d to 1 to show the hidden files
reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced /v Hidden /t REG_DWORD /d 0 /f
mshta vbscript:Execute("msgbox ""Now You Can't See Me!"":close")

endlocal
