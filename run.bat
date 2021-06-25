rem set n=%1
set s_path=%1
FINDSTR "a=10" %s_path%\myfile.txt
if %errorlevel%==0 (
call run_helloworld.bat "helloworld.py"
) else (
GOTO error)
GOTO end
:error
    echo "a!=20"
:end