#!/bin/bash

# PyQuest - Quick Launch Script
# Run this to start your learning session!

echo "🐍 Starting PyQuest..."
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "⚠️  .env file not found!"
    echo "📝 Creating from template..."
    cp .env.example .env
    echo "✅ Created .env file"
    echo ""
    echo "⚠️  IMPORTANT: Edit .env with your information before continuing!"
    echo "   Run: open .env"
    echo ""
    exit 1
fi

# Check if dependencies are installed
if ! python3 -c "import flask" 2>/dev/null; then
    echo "📦 Installing dependencies..."
    pip3 install -r requirements.txt
    echo ""
fi

# Start the application
echo "🚀 Launching PyQuest..."
echo ""
python3 app.py
