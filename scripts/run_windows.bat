@echo off
echo Activating virtual environment...
cd /d "%~dp0.."
call venv\Scripts\activate

echo Running bot...
python main.py

pause
