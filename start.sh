#!/bin/bash

# Stroke Predictor - Start Backend and Frontend

echo "🏥 Starting Stroke Predictor Application"
echo "========================================"

# Function to check if port is in use
check_port() {
    if lsof -Pi :$1 -sTCP:LISTEN -t >/dev/null; then
        echo "⚠️  Port $1 is already in use. Please stop the existing service first."
        return 1
    fi
    return 0
}

# Check if ports are available
if ! check_port 5001; then
    exit 1
fi

if ! check_port 3000; then
    exit 1
fi

echo
echo "📦 Installing/Updating Backend Dependencies..."
cd backend
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi
source venv/bin/activate
pip install -r requirements.txt

echo
echo "📦 Installing/Updating Frontend Dependencies..."
cd ../frontend
npm install

echo
echo "🚀 Starting Backend Server (Port 5001)..."
cd ../backend
source venv/bin/activate
python app.py &
BACKEND_PID=$!

echo "🚀 Starting Frontend Server (Port 3000)..."
cd ../frontend
npm start &
FRONTEND_PID=$!

echo
echo "✅ Both servers are starting up..."
echo "🌐 Frontend: http://localhost:3000"
echo "🔧 Backend API: http://localhost:5001"
echo
echo "Press Ctrl+C to stop both servers"

# Function to cleanup on exit
cleanup() {
    echo
    echo "🛑 Stopping servers..."
    kill $BACKEND_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    wait
    echo "✅ All servers stopped"
}

# Set up cleanup on script exit
trap cleanup SIGINT SIGTERM

# Wait for both processes
wait