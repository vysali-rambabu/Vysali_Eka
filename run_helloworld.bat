REM --------- %1 %2 %3 and so on takes the args that are passed along with the batch file separated by a space--
set x=%1   
set /p n=Enter runner name: 
echo %n%
python -c "exec(open('%n%').read())"
for %%a in ("%~dp0..") do set PATH_TWO_LEVELS_UP=%%~fa
echo %PATH_TWO_LEVELS_UP%
set y=%~dp0..\..
echo %y%