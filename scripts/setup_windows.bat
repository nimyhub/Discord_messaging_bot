@echo off
echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing dependencies from requirements.txt...
pip install --upgrade pip
pip install -r requirements.txt

echo Setup complete. You can now run the bot using run.bat
pause