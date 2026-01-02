@echo off
echo ========================================
echo   SEO Alt Text Generator Server
echo ========================================
echo.
echo Starting server...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

REM Check if requests module is installed
python -c "import requests" >nul 2>&1
if errorlevel 1 (
    echo Installing required Python package: requests
    echo.
    pip install requests
    echo.
)

REM Start the server
echo Server will start at http://localhost:8000
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.

python server.py

pause
