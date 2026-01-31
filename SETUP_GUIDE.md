# 🐍 PyQuest Setup Guide for Beginners

Welcome! This guide will walk you through setting up PyQuest step by step. No prior experience needed!

## 📋 What You'll Need

1. **A Computer** (Mac, Windows, or Linux)
2. **Internet Connection**
3. **30 minutes for setup**
4. **Enthusiasm to learn!** 🚀

---

## Step 1: Install Python (5 minutes)

### Check if Python is Already Installed

Open your **Terminal** (Mac) or **Command Prompt** (Windows):

**Mac:**
- Press `Cmd + Space`
- Type "Terminal"
- Press Enter

**Windows:**
- Press `Windows key`
- Type "cmd"
- Press Enter

In the terminal/command prompt, type:
```bash
python3 --version
```

If you see something like "Python 3.x.x", you're good! Skip to Step 2.

### If Python is NOT Installed

1. Go to https://www.python.org/downloads/
2. Click the big yellow "Download Python" button
3. Run the installer
4. **IMPORTANT:** Check the box that says "Add Python to PATH"
5. Click "Install Now"
6. Wait for installation to complete

**Verify Installation:**
```bash
python3 --version
```

---

## Step 2: Install pip (Python Package Manager)

pip usually comes with Python. Verify it's installed:

```bash
pip3 --version
```

If you see a version number, you're good!

If not, download it:
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```

---

## Step 3: Navigate to the Project

Open Terminal/Command Prompt and type:

```bash
cd /Users/josiah.cline/Documents/python-learning-platform
```

**Explanation:** `cd` means "change directory" (go into a folder)

**Verify you're in the right place:**
```bash
pwd
```

You should see: `/Users/josiah.cline/Documents/python-learning-platform`

---

## Step 4: Install Dependencies (2 minutes)

Install all the Python packages PyQuest needs:

```bash
pip3 install -r requirements.txt
```

This will install:
- Flask (web framework)
- APScheduler (for reminders)
- PyYAML (for loading challenges)
- And more!

**Wait 1-2 minutes** while packages download and install.

---

## Step 5: Configure Your Settings (5 minutes)

### Create Your Environment File

```bash
cp .env.example .env
```

**Explanation:** This copies the example file to create your personal settings file.

### Edit Your Settings

Open the `.env` file in a text editor:

**Mac:**
```bash
open -e .env
```

**Windows:**
```bash
notepad .env
```

**Or:** Open it in VS Code if you have it installed.

### Fill in Your Information

**Required Settings:**
```bash
USER_NAME=Josie Cline
USER_EMAIL=josiah.cline@scale.com
```

**Daily Reminder Time** (when you want to be reminded):
```bash
DAILY_REMINDER_TIME=09:00
```
Use 24-hour format: 09:00 = 9 AM, 14:00 = 2 PM, etc.

**Weekly Report Day** (0=Monday, 6=Sunday):
```bash
WEEKLY_REPORT_DAY=0
```

### Optional: Email Notifications

If you want email reminders:

1. **Gmail Users:**
   - Go to https://myaccount.google.com/apppasswords
   - Sign in
   - Create an app password for "Mail"
   - Copy the password (16 characters)

2. **Add to .env:**
```bash
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-16-char-app-password
```

### Optional: Slack Notifications

If you want Slack reminders:

1. Create a Slack webhook:
   - Go to https://api.slack.com/messaging/webhooks
   - Click "Create your Slack app"
   - Follow the instructions

2. **Add to .env:**
```bash
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/YOUR/WEBHOOK/URL
```

**Save and close the file!**

---

## Step 6: Start PyQuest! (1 minute)

Run the application:

```bash
python3 app.py
```

You should see:
```
╔═══════════════════════════════════════════════════╗
║                                                   ║
║          🐍 PyQuest Learning Platform 🐍          ║
║                                                   ║
║   Your journey to Python mastery starts now!     ║
║                                                   ║
║   📍 Open your browser to:                        ║
║      http://localhost:5000                       ║
║                                                   ║
║   Press Ctrl+C to stop the server                ║
║                                                   ║
╚═══════════════════════════════════════════════════╝
```

---

## Step 7: Open in Browser

1. Open your web browser (Chrome, Firefox, Safari, etc.)
2. Go to: **http://localhost:5000**
3. You should see the PyQuest dashboard!

---

## 🎉 You're All Set!

### Quick Start Guide

1. **Start the server:** `python3 app.py`
2. **Open browser:** http://localhost:5000
3. **Click "Today's Challenge"**
4. **Write code** in the editor
5. **Click "Run Tests"** to check your solution
6. **Click "Submit"** when all tests pass!

### Daily Routine

1. Open Terminal
2. Navigate to project: `cd /Users/josiah.cline/Documents/python-learning-platform`
3. Start server: `python3 app.py`
4. Open browser: http://localhost:5000
5. Complete today's challenge!
6. When done, press `Ctrl+C` in Terminal to stop the server

---

## 🆘 Troubleshooting

### "Command not found: python3"
**Fix:** Install Python (see Step 1)

### "Port 5000 already in use"
**Fix:** Something else is using that port. 
1. Open `app.py`
2. Find the line: `PORT=5000`
3. Change to `PORT=5001` (or any number 5001-9999)
4. Try again

### "Module not found"
**Fix:** Install dependencies again:
```bash
pip3 install -r requirements.txt
```

### "Permission denied"
**Fix:** Try adding `sudo`:
```bash
sudo pip3 install -r requirements.txt
```
(You'll be asked for your computer password)

### Can't open http://localhost:5000
**Fix:** 
1. Make sure the server is running (you should see the PyQuest banner)
2. Try http://127.0.0.1:5000 instead
3. Check your firewall isn't blocking it

---

## 📚 Next Steps

1. **Complete your first challenge!**
2. **Install VS Code** for a better coding experience: https://code.visualstudio.com/
3. **Learn Git** to save your code: Read the Git section in README.md
4. **Join the community** (if available)

---

## 🎯 Tips for Success

- **Be consistent:** Do challenges daily, even if only 20 minutes
- **Don't skip challenges:** Each builds on the previous ones
- **Use hints wisely:** Try for 10 minutes before looking
- **Read error messages:** They tell you what's wrong!
- **Ask questions:** No question is too basic
- **Celebrate progress:** Every challenge completed is a win!

---

## 📧 Need Help?

- Check the README.md for more detailed info
- Look at the Resources page in PyQuest
- Review the Troubleshooting section

---

**Ready to start your Python journey? Let's go! 🚀**
