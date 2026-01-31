# 🎯 Quick Start Guide - PyQuest

**Get started in 5 minutes!**

## 1️⃣ Installation (One Time)

```bash
cd /Users/josiah.cline/Documents/python-learning-platform
bash setup.sh
```

This installs everything you need automatically.

## 2️⃣ Configuration (One Time)

Edit your `.env` file with your information:

```bash
open .env
```

**Required settings:**
- `USER_NAME` - Your name
- `USER_EMAIL` - Your email
- `DAILY_REMINDER_TIME` - When to remind you (e.g., 09:00)

**Optional settings:**
- Email credentials (for email reminders)
- Slack webhook (for Slack notifications)

## 3️⃣ Start Learning! (Every Day)

```bash
bash start.sh
```

Then open your browser to: **http://localhost:5000**

## 🎮 Daily Workflow

1. Open Terminal
2. Run: `bash start.sh`
3. Open browser: http://localhost:5000
4. Complete today's challenge
5. When done: Press `Ctrl+C` in Terminal

## 🆘 Need Help?

- **Detailed setup:** See `SETUP_GUIDE.md`
- **Deployment:** See `DEPLOYMENT.md`
- **Full docs:** See `README.md`

## 🐛 Quick Troubleshooting

**"python3: command not found"**
→ Install Python from https://www.python.org/downloads/

**"pip3: command not found"**
→ Run: `python3 -m ensurepip --upgrade`

**"Port 5000 already in use"**
→ Change PORT in .env file to 5001

**"Module not found"**
→ Run: `pip3 install -r requirements.txt`

## 🚀 What's Next?

1. Complete Week 1 challenges
2. Set up daily reminders
3. Deploy online (see DEPLOYMENT.md)
4. Join the learning community

**Happy coding!** 🐍
