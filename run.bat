set param2=%2
echo %param1%
echo %param2%
if "%1%"=="" (
	GOTO error)
set param1=%1hey
echo %param1%
:error
	echo error