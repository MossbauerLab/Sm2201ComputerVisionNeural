:: VARIABLES
SET ROOT_DIRECTORY=".."
SET VENV_DIRECTORY="venv"
:: SET PYTHON="%VENV_DIRECTORY%\p"
SET PIP="%VENV_DIRECTORY%\Scripts\pip"
SET REQUIREMENTS_FILE="%ROOT_DIRECTORY%\requirements.txt"

rd /s /q %VENV_DIRECTORY%
virtualenv %VENV_DIRECTORY%
%VENV_DIRECTORY%\Scripts\activate.bat
%PIP% install -r %REQUIREMENTS_FILE%