@echo off
set /p killing="D0 y0u want t0 kill startup apps? (y/n) "
if %killing%==n (echo Sure, I will spare them... F0R N0WWW!!!)
if %killing%==y (
taskkill /im "PhoneExperienceHost.exe" /t /f
echo RIP Phone Link...
taskkill /im "Grammarly.Desktop.exe" /t /f
echo RIP Grammarly...
taskkill /im "WiseMemoryOptimzer.exe" /t /f
echo RIP Wise Memory Optimizer...
taskkill /im "DSATray.exe" /t /f
echo RIP Intel Driver Assistant...
taskkill /im "Spotify.exe" /t /f
echo RIP Spotify...
REM taskkill /im "Cloudflare WARP.exe" /t /f
REM echo RIP Cloudflare WARP...
)

set /p more_killing="D0 y0u want t0 kill any m0re pr0cesses? (y/n) "
if %more_killing%==n (echo G00dbye! Press any key t0 exit... && pause>nul)
if %more_killing%==y (
rem The part below this line is not working. Will have to find a way to pass the variable "search" into the find / findstr command.
set /p search="G0 0n, enter the applicati0n name. I will search f0r it's pr0cess: "
tasklist /v | findstr /i "!search!"
echo Done!
pause>nul
)

