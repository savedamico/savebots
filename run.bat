@ECHO OFF
python3 --version 3 > NUL
if errorlevel 1 goto tryPython3

python3 -m pip3 install -r requirements.txt
cd src
python3 main.py

goto:eof

:tryPython3
ECHO Trying python command.
python --version 3 > NUL
if errorlevel 1 goto errorNoPython

python -m pip install -r requirements.txt
cd src
python main.py

goto:eof

:errorNoPython
ECHO.
ECHO Error^: Python not installed
"C:\Program Files\used\systems\innoventiq\accumanager\required\excutables\python-3.7.3-amd64.exe"

python --version 3 > NUL
if errorlevel 1 goto tryPython3