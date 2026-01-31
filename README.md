# 🐍 PyQuest - Your Python Learning Journey

**Welcome!** This is your personal Python learning platform designed to take you from complete beginner to Scale AI Frontend Engineer level in 6 months.

## 🎯 What This Does

- **Daily Challenges**: 30-60 minute Python exercises tailored to your level
- **Progress Tracking**: See your streak, completion rate, and skill development
- **Interactive Learning**: Beautiful HTML game interface - learn by doing!
- **Reminders**: Daily notifications and weekly progress reports
- **Real Exam Prep**: Curriculum designed around actual Scale AI coding interviews

## 📚 What You'll Learn

### Months 1-2: Foundations
- Variables, data types, and operators
- Control flow (if/else, loops)
- Functions and scope
- Lists, tuples, dictionaries, sets
- String manipulation

### Months 3-4: Intermediate Skills
- File I/O and error handling
- Object-oriented programming (classes, inheritance)
- Working with APIs and JSON
- List comprehensions and generators
- Regular expressions

### Months 5-6: Advanced & Interview Prep
- Algorithms (sorting, searching, recursion)
- Data structures (stacks, queues, trees)
- Problem-solving patterns
- Code optimization
- **Mock Scale AI coding interviews**

## 🚀 Quick Start (5 Minutes)

### Step 1: Install Python
Check if you have Python installed:
```bash
python3 --version
```

If you see "Python 3.x.x", you're good! If not, download from [python.org](https://www.python.org/downloads/)

### Step 2: Install Dependencies
```bash
cd /Users/josiah.cline/Documents/python-learning-platform
pip3 install -r requirements.txt
```

### Step 3: Set Up Your Environment
```bash
cp .env.example .env
```

Edit `.env` with your details (see "Configuration" section below)

### Step 4: Start Learning!
```bash
python3 app.py
```

Open your browser to: **http://localhost:5000**

## 🔧 Configuration

Edit your `.env` file with these settings:

```bash
# Your name and email for progress tracking
USER_NAME=Josie Cline
USER_EMAIL=josiah.cline@scale.com

# Daily reminder time (24-hour format, e.g., 09:00 for 9 AM)
DAILY_REMINDER_TIME=09:00

# Weekly report day (Monday=0, Sunday=6)
WEEKLY_REPORT_DAY=0

# Email settings (optional - for reminders)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-app-password

# Slack webhook (optional - for notifications)
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/YOUR/WEBHOOK/URL
```

## 🎮 How to Use

1. **Start Your Day**: Open http://localhost:5000
2. **Get Today's Challenge**: Click "Today's Challenge"
3. **Code Your Solution**: Write Python code in the interactive editor
4. **Test & Submit**: Run tests to check your solution
5. **Track Progress**: View your dashboard for stats and streaks

## 📖 Beginner's Guide to Tools

### What is Git?
Git is like "track changes" for code. It saves snapshots of your work so you can:
- Go back to previous versions
- Share code with others
- Work on multiple features at once

**Basic commands you'll use:**
```bash
git status          # See what changed
git add .           # Stage all changes
git commit -m "message"  # Save a snapshot
git push            # Upload to GitHub
```

### What is VS Code?
VS Code is a text editor for writing code. Think of it like Microsoft Word, but for programming.

**Install it**: [code.visualstudio.com](https://code.visualstudio.com/)

**Useful shortcuts:**
- `Cmd + S`: Save file
- `Cmd + /`: Comment/uncomment lines
- `Cmd + F`: Find text
- `Cmd + Shift + P`: Open command palette

### What is Terminal/Command Line?
The terminal lets you control your computer with text commands instead of clicking.

**On Mac**: Open "Terminal" app (Cmd + Space, type "Terminal")

**Basic commands:**
```bash
cd folder_name      # Change directory (go into a folder)
ls                  # List files in current folder
pwd                 # Print working directory (where am I?)
mkdir folder_name   # Make a new folder
python3 file.py     # Run a Python file
```

### What is pip?
`pip` is Python's package installer. It downloads code libraries that others have written so you don't have to reinvent the wheel.

**Example:**
```bash
pip3 install flask   # Installs the Flask web framework
```

## 🗂️ Project Structure

```
python-learning-platform/
├── app.py                    # Main web server
├── static/                   # CSS, JavaScript, images
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── app.js
├── templates/                # HTML pages
│   ├── index.html           # Homepage/dashboard
│   ├── challenge.html       # Daily challenge page
│   └── progress.html        # Progress tracking
├── challenges/               # Python challenges database
│   ├── __init__.py
│   ├── loader.py
│   └── data/
│       ├── week_001.yaml    # Week 1 challenges
│       ├── week_002.yaml    # Week 2 challenges
│       └── ...
├── grader/                   # Auto-grading system
│   ├── __init__.py
│   └── test_runner.py
├── reminders/                # Notification system
│   ├── __init__.py
│   ├── scheduler.py
│   └── notifier.py
├── .env                      # Your secrets (NOT in git)
├── .env.example             # Template for .env
└── requirements.txt          # Python dependencies
```

## 📊 Tracking Your Progress

Your progress is saved locally in `user_progress.json`. This includes:
- Challenges completed
- Current streak
- Time spent learning
- Skills mastered

**Weekly Reports** are automatically generated and include:
- Challenges completed this week
- Time invested
- Skills practiced
- Next week's focus areas
- Motivational insights

## 🆘 Troubleshooting

### "Command not found: python3"
**Fix**: Install Python from [python.org](https://www.python.org/downloads/)

### "Port 5000 already in use"
**Fix**: Change the port in `app.py` (line with `app.run()`)

### "Module not found"
**Fix**: Install dependencies: `pip3 install -r requirements.txt`

### "Can't connect to database"
**Fix**: Make sure you're in the project folder when running `python3 app.py`

## 🎓 Learning Resources

- **Python Docs**: [docs.python.org](https://docs.python.org/)
- **Practice Problems**: Built into PyQuest!
- **Video Tutorials**: [Real Python](https://realpython.com/)
- **Scale AI Interview Prep**: Built into Months 5-6 curriculum

## 📞 Support

Questions? Issues? Want to customize your learning path?

1. Check the documentation in `/docs`
2. Look at example solutions in `/solutions` (after completing challenges)
3. Review the troubleshooting guide above

## 🎉 Your Learning Journey Starts Now!

Remember:
- **Consistency beats intensity**: 30 minutes daily > 3 hours once a week
- **Mistakes are learning**: Every error teaches you something
- **Progress, not perfection**: Focus on understanding, not memorizing
- **Ask questions**: Use comments in your code to note confusions

**Ready to start?** Run `python3 app.py` and visit http://localhost:5000

Happy coding! 🚀
