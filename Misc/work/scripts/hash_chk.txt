@echo off
set file_path=D:\Users\5herl0ck\Downloads
cd /d %file_path%

:start
echo If y0ur file's path is different, change it n0w.
echo The current direct0ry is: %cd%
echo If y0u want t0 stay in the current direct0ry, type a d0t (.)
echo.

set /p file_path=
cd /d %file_path%
echo You are currently in: %cd%
echo.

set /p traversal="Still want to change y0ur current direct0ry (y/n)? "
if %traversal%==y (goto start)
if %traversal%==n (echo 0nwards, s0ldier!!)

set /p show_files="D0 y0u want t0 see all files in this direct0ry (y/n)? "
if %show_files%==y (@echo on && dir "%file_path%" && @echo off)
if %show_files%==n (echo W0w, y0u have a g00d mem0ry! && echo.)

set /p file_name="Enter any file name fr0m the ab0ve list (You can type the starting part and hit TAB to autocomplete): "
echo.
set hash_algo=MD5
set /p hash_algo="Enter hash alg0rithm (MD5, SHA1, SHA256, etc), type md5 if you're not sure: "
echo.
certutil -hashfile %file_name% %hash_algo%
echo.

set /p next_step="D0 y0u want t0 find the hash f0r an0ther file (y/n)? "
echo.
if %next_step%==y (goto start)
if %next_step%==n (echo G00dbye! Press any key t0 exit... && pause>nul)