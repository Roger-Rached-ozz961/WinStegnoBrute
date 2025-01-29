@echo off
:: Check if the virtual environment is activated, otherwise activate it
IF NOT DEFINED VIRTUAL_ENV (
    echo Activating virtual environment...
    call venv\Scripts\activate
)

:: Run the script directly with Python
echo Running WinStegnoBrute.py script...
powershell -NoExit -Command "python .\WinStegnoBrute.py"
