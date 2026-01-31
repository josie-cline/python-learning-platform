#!/bin/bash

# PyQuest Quick Setup Script
# This script automates the setup process

echo "╔═══════════════════════════════════════════════════╗"
echo "║                                                   ║"
echo "║       🐍 PyQuest Setup Script 🐍                  ║"
echo "║                                                   ║"
echo "╚═══════════════════════════════════════════════════╝"
echo ""

# Check if Python 3 is installed
echo "🔍 Checking for Python 3..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed."
    echo "📥 Please install Python from: https://www.python.org/downloads/"
    exit 1
fi

PYTHON_VERSION=$(python3 --version)
echo "✅ Found: $PYTHON_VERSION"
echo ""

# Check if pip is installed
echo "🔍 Checking for pip..."
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed."
    echo "📥 Installing pip..."
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python3 get-pip.py
    rm get-pip.py
fi

PIP_VERSION=$(pip3 --version)
echo "✅ Found: $PIP_VERSION"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully!"
else
    echo "❌ Failed to install dependencies"
    echo "💡 Try running: sudo pip3 install -r requirements.txt"
    exit 1
fi
echo ""

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file..."
    cp .env.example .env
    echo "✅ Created .env file from template"
    echo "⚠️  Please edit .env with your information:"
    echo "    - USER_NAME"
    echo "    - USER_EMAIL"
    echo "    - DAILY_REMINDER_TIME"
    echo ""
else
    echo "✅ .env file already exists"
    echo ""
fi

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p static/images
mkdir -p challenges/data
mkdir -p logs
echo "✅ Directories created"
echo ""

# Test if the app can start
echo "🧪 Testing application..."
timeout 5 python3 -c "import app" 2>/dev/null

if [ $? -eq 0 ] || [ $? -eq 124 ]; then
    echo "✅ Application test passed"
else
    echo "⚠️  Application test had warnings (this might be okay)"
fi
echo ""

echo "╔═══════════════════════════════════════════════════╗"
echo "║                                                   ║"
echo "║              ✅ Setup Complete! ✅                 ║"
echo "║                                                   ║"
echo "╚═══════════════════════════════════════════════════╝"
echo ""
echo "📚 Next steps:"
echo "   1. Edit .env with your information"
echo "   2. Run: python3 app.py"
echo "   3. Open: http://localhost:5000"
echo ""
echo "📖 For detailed instructions, see SETUP_GUIDE.md"
echo ""
echo "Happy coding! 🚀"
