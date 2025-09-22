@echo off
title Stroke Predictor Application

echo 🏥 Starting Stroke Predictor Application
echo ========================================

echo.
echo 📦 Installing/Updating Backend Dependencies...
cd backend
if not exist "venv" (
    echo Creating Python virtual environment...
    python -m venv venv
)
call venv\Scripts\activate
pip install -r requirements.txt

echo.
echo 📦 Installing/Updating Frontend Dependencies...
cd ..\frontend
call npm install

echo.
echo 🚀 Starting Backend Server (Port 5001)...
cd ..\backend
call venv\Scripts\activate
start "Backend Server" python app.py

echo 🚀 Starting Frontend Server (Port 3000)...
cd ..\frontend
start "Frontend Server" npm start

echo.
echo ✅ Both servers are starting up...
echo 🌐 Frontend: http://localhost:3000
echo 🔧 Backend API: http://localhost:5001
echo.
echo Press any key to continue...
pause > nul