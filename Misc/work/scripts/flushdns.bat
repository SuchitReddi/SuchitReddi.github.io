@echo off

REM Setting the window size to very small (Note: If the columns is less than 15, it isn't working)
mode con Lines=1 Cols=15
REM Clear DNS cache
ipconfig /flushdns

mshta vbscript:Execute("msgbox ""You're doing a better job at clearing your tracks! Good job."":close")
