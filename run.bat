REM I'm not sure whether this batch file will work for everyone

cd src
python Main.py
if ERRORLEVEL 1 goto ERROR
EXIT %errorlevel%

:ERROR
py Main.py