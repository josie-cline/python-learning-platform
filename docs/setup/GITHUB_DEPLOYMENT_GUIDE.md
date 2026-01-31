# 🚀 Complete GitHub & Deployment Setup

**Follow these steps to get your PyQuest platform online with a URL!**

---

## Part 1: Set Up GitHub (10 minutes)

### Step 1: Create GitHub Account

1. Go to https://github.com
2. Click "Sign up"
3. Enter your email: `josiah.cline@scale.com`
4. Create a password
5. Choose a username (e.g., `josie-cline` or `josiah-cline`)
6. Complete verification
7. Verify your email

### Step 2: Create New Repository

1. Once logged in, click the "+" icon (top right)
2. Select "New repository"
3. Fill in details:
   - **Repository name:** `pyquest-learning-platform`
   - **Description:** "My 6-month Python learning journey to become a Scale AI Field Engineer"
   - **Visibility:** Choose "Public" (to show your progress!) or "Private"
   - **DON'T** check "Initialize with README" (we already have one)
4. Click "Create repository"

### Step 3: Connect Your Local Project to GitHub

Open Terminal and run these commands:

```bash
# Navigate to your project
cd /Users/josiah.cline/Documents/python-learning-platform

# Add your GitHub repository (replace YOUR-USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR-USERNAME/pyquest-learning-platform.git

# Push your code to GitHub
git push -u origin main
```

**Example:**
```bash
git remote add origin https://github.com/josie-cline/pyquest-learning-platform.git
git push -u origin main
```

You'll be asked for your GitHub credentials. Use your:
- **Username:** Your GitHub username
- **Password:** Your GitHub password OR Personal Access Token (recommended)

### Step 4: Create Personal Access Token (Recommended)

If password doesn't work, create a token:

1. Go to https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Name: "PyQuest Deployment"
4. Select scopes: `repo` (all)
5. Click "Generate token"
6. **COPY THE TOKEN** (you won't see it again!)
7. Use this as your password when pushing

### Step 5: Verify on GitHub

1. Go to your repository on GitHub
2. You should see all your files!
3. README.md should be displayed on the main page

---

## Part 2: Deploy to Render (15 minutes) - RECOMMENDED

**Why Render?** Free, easy, and perfect for beginners!

### Step 1: Create Render Account

1. Go to https://render.com
2. Click "Get Started"
3. Sign up with GitHub (easier!) or email
4. If using GitHub, authorize Render to access your repositories

### Step 2: Create New Web Service

1. Click "New +" (top right)
2. Select "Web Service"
3. Connect your repository:
   - If you signed up with GitHub: Select `pyquest-learning-platform`
   - If not: Connect GitHub account first, then select repo

### Step 3: Configure Service

Fill in these settings:

- **Name:** `pyquest-learning` (or your preferred name)
- **Region:** Choose closest to you
- **Branch:** `main`
- **Root Directory:** Leave blank
- **Runtime:** `Python 3`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`
- **Instance Type:** `Free`

### Step 4: Add Environment Variables

Scroll down to "Environment Variables" section.

Click "Add Environment Variable" for each:

```
USER_NAME = Josie Cline
USER_EMAIL = josiah.cline@scale.com
TARGET_ROLE = Scale AI Field Engineer
DAILY_REMINDER_TIME = 09:00
WEEKLY_REPORT_DAY = 0
WEEKLY_REPORT_TIME = 10:00
PORT = 10000
DEBUG = false
TIMEZONE = America/Los_Angeles
```

**Optional (if you set them up):**
```
SMTP_SERVER = smtp.gmail.com
SMTP_PORT = 587
SMTP_USERNAME = your-email@gmail.com
SMTP_PASSWORD = your-app-password
SLACK_WEBHOOK_URL = your-slack-webhook-url
```

### Step 5: Deploy!

1. Click "Create Web Service"
2. Render will start building your app
3. Watch the logs - it takes 2-5 minutes
4. When you see "Deploy live" - you're done!

### Step 6: Get Your URL

Your PyQuest URL will be:

```
https://pyquest-learning.onrender.com
```

(Or whatever name you chose)

**⭐ Bookmark this URL!**

---

## Part 3: Alternative - Deploy to Heroku

### Quick Heroku Setup

```bash
# Install Heroku CLI (Mac)
brew tap heroku/brew && brew install heroku

# Login
heroku login

# Create app
cd /Users/josiah.cline/Documents/python-learning-platform
heroku create pyquest-learning

# Set environment variables
heroku config:set USER_NAME="Josie Cline"
heroku config:set USER_EMAIL="josiah.cline@scale.com"
heroku config:set DAILY_REMINDER_TIME="09:00"
# ... add all other variables

# Deploy
git push heroku main

# Open app
heroku open
```

Your URL: `https://pyquest-learning.herokuapp.com`

---

## Part 4: Test Your Deployment

Once deployed, test everything:

1. ✅ **Visit your URL**
   - Homepage loads
   - Your name appears

2. ✅ **Try Today's Challenge**
   - Click "Today's Challenge"
   - Code editor appears
   - Can type code

3. ✅ **Test Code Execution**
   - Write simple code: `def hello_world(): print("Hello, World!")`
   - Click "Run Tests"
   - See results

4. ✅ **Check All Pages**
   - Dashboard
   - Curriculum
   - Progress
   - Resources

---

## Part 5: Share Your Progress

### Add README Badge

Add this to your GitHub README to show it's live:

```markdown
![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen)
[View Live Site](https://your-url-here.onrender.com)
```

### Share Your Journey

Share your URL with:
- Friends and family
- LinkedIn (great for job hunting!)
- Twitter/X
- Scale AI team (show your dedication!)

---

## Part 6: Keeping It Updated

### When You Make Changes

```bash
# Navigate to project
cd /Users/josiah.cline/Documents/python-learning-platform

# Check what changed
git status

# Add changes
git add .

# Commit
git commit -m "Add new challenges" 

# Push to GitHub
git push origin main
```

**Render** automatically redeploys when you push!
**Heroku** also auto-deploys (if you enabled it).

---

## 🎉 You Did It!

You now have:
- ✅ Code on GitHub
- ✅ Live website with a URL
- ✅ Automatic deployments
- ✅ Professional portfolio piece

**Your URL is your learning platform - access it from anywhere!**

---

## 🐛 Troubleshooting Deployment

### Build Failed

**Check logs:**
- Render: Click "Logs" tab
- Heroku: `heroku logs --tail`

**Common issues:**
- Missing dependency in `requirements.txt`
- Python version incompatible
- Environment variable typo

### App Crashes

**Check:**
- All environment variables are set
- No syntax errors in code
- Logs for specific error messages

### Free Tier Limitations

**Render Free Tier:**
- Sleeps after 15 min inactivity
- First load takes ~30 seconds
- 750 hours/month free

**Solution:** Upgrade to paid ($7/mo) for always-on

### Can't Push to GitHub

**Error: "remote: Permission denied"**
- Use Personal Access Token instead of password
- Check token has `repo` permissions

**Error: "remote: Repository not found"**
- Check repository name is correct
- Make sure you're logged into correct GitHub account

---

## 📝 Next Steps

1. ✅ **Share your URL with me!** (Post it in chat)
2. 📧 **Set up email reminders** (add SMTP variables)
3. 💻 **Complete Week 1 challenges**
4. 🎯 **Track your 6-month progress**
5. 📱 **Access from any device** using your URL

**Need help?** Let me know and I'll troubleshoot with you!

---

## 🎓 What This Means

You've just:
1. Created a full-stack web application
2. Used version control (Git)
3. Deployed to production
4. Got a live URL

**These are professional software engineering skills!** 🚀

Keep learning, and in 6 months you'll be ready for that Scale AI interview!
