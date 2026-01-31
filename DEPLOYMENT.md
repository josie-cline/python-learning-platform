# 🚀 Deployment Guide - Getting Your URL

This guide shows you how to deploy PyQuest online so you can access it from anywhere!

## Option 1: Render (Recommended - Free & Easy)

**Why Render?**
- Free tier available
- Easy setup
- Automatic HTTPS
- Good for beginners

### Steps:

1. **Push to GitHub** (see below)

2. **Create Render Account**
   - Go to https://render.com
   - Sign up (use GitHub login for easy integration)

3. **Create New Web Service**
   - Click "New +"
   - Select "Web Service"
   - Connect your GitHub repository

4. **Configure Service**
   - Name: `pyquest-learning`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Instance Type: `Free`

5. **Add Environment Variables**
   - Click "Environment" tab
   - Add all variables from your `.env` file
   - Click "Save Changes"

6. **Deploy!**
   - Click "Create Web Service"
   - Wait 2-5 minutes for deployment
   - Your URL will be: `https://pyquest-learning.onrender.com`

**Note:** Free tier sleeps after inactivity. First load takes ~30 seconds.

---

## Option 2: Heroku (Also Free)

**Why Heroku?**
- Very popular
- Good documentation
- Free tier available

### Steps:

1. **Install Heroku CLI**
   ```bash
   # Mac
   brew install heroku/brew/heroku
   
   # Windows
   # Download from: https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create Heroku App**
   ```bash
   cd /Users/josiah.cline/Documents/python-learning-platform
   heroku create pyquest-learning
   ```

4. **Add Procfile**
   Create a file named `Procfile` (no extension):
   ```
   web: gunicorn app:app
   ```

5. **Set Environment Variables**
   ```bash
   heroku config:set USER_NAME="Your Name"
   heroku config:set USER_EMAIL="your.email@example.com"
   # ... add all your .env variables
   ```

6. **Deploy**
   ```bash
   git push heroku main
   ```

7. **Open Your App**
   ```bash
   heroku open
   ```
   Your URL: `https://pyquest-learning.herokuapp.com`

---

## Option 3: PythonAnywhere (Beginner-Friendly)

**Why PythonAnywhere?**
- Designed for Python apps
- Very simple setup
- Free tier: `username.pythonanywhere.com`

### Steps:

1. **Create Account**
   - Go to https://www.pythonanywhere.com
   - Sign up for free account

2. **Upload Code**
   - Go to "Files" tab
   - Upload your project files
   - Or clone from GitHub

3. **Create Web App**
   - Go to "Web" tab
   - Click "Add a new web app"
   - Choose "Flask"
   - Python version: 3.x

4. **Configure**
   - Set working directory to your project
   - Set WSGI file to point to `app.py`
   - Add environment variables in "Environment" section

5. **Reload**
   - Click "Reload" button
   - Your URL: `https://yourusername.pythonanywhere.com`

---

## Option 4: Local Network Access (No Internet Required)

**Why Local?**
- No deployment needed
- Free
- Full control
- Good for learning

### Steps:

1. **Find Your Local IP**
   ```bash
   # Mac/Linux
   ifconfig | grep "inet "
   
   # Windows
   ipconfig
   ```
   Look for something like `192.168.1.xxx`

2. **Start PyQuest**
   ```bash
   python3 app.py
   ```

3. **Access from Same Network**
   - On any device on your WiFi
   - Open browser
   - Go to: `http://YOUR-IP:5000`
   - Example: `http://192.168.1.105:5000`

**Note:** This only works on your local network (home/office WiFi)

---

## Setting Up GitHub (Required for Most Options)

### First Time Git Setup

1. **Install Git**
   ```bash
   # Mac (if not installed)
   brew install git
   
   # Windows
   # Download from: https://git-scm.com/download/win
   ```

2. **Configure Git**
   ```bash
   git config --global user.name "Josie Cline"
   git config --global user.email "josiah.cline@scale.com"
   ```

3. **Create GitHub Account**
   - Go to https://github.com
   - Sign up for free account

### Push Your Project to GitHub

1. **Create Repository on GitHub**
   - Go to https://github.com/new
   - Name: `pyquest-learning-platform`
   - Description: "My Python learning journey"
   - Set to Public or Private
   - DON'T initialize with README (we have one)
   - Click "Create repository"

2. **Push Your Code**
   ```bash
   cd /Users/josiah.cline/Documents/python-learning-platform
   
   # Add files
   git add .
   
   # Commit
   git commit -m "Initial commit - PyQuest learning platform"
   
   # Add remote
   git remote add origin https://github.com/YOUR-USERNAME/pyquest-learning-platform.git
   
   # Push
   git push -u origin main
   ```

3. **Verify**
   - Refresh your GitHub repository page
   - You should see all your files!

---

## Additional Requirements for Deployment

Add this to `requirements.txt`:

```
gunicorn==21.2.0
```

This is needed for production deployment.

---

## Environment Variables Security

**IMPORTANT:** Never commit your `.env` file!

Your `.gitignore` already excludes it, but double-check:

```bash
# Verify .env is not tracked
git status
```

`.env` should NOT appear in the list.

---

## Costs

| Platform | Free Tier | Paid |
|----------|-----------|------|
| Render | Yes (sleeps after inactivity) | $7/mo |
| Heroku | Yes (limited hours) | $7/mo |
| PythonAnywhere | Yes (.pythonanywhere.com) | $5/mo |
| Local Network | Free | Free |

**Recommendation for Learning:** Start with Local Network or Render free tier!

---

## Testing Your Deployment

Once deployed, test these features:

1. ✅ Homepage loads
2. ✅ Can view today's challenge
3. ✅ Can submit code and run tests
4. ✅ Progress is saved
5. ✅ All pages work (dashboard, curriculum, progress, resources)

---

## Troubleshooting Deployment

### "Application Error"
- Check logs: `heroku logs --tail` (Heroku)
- Verify all environment variables are set
- Make sure `gunicorn` is in requirements.txt

### "Module not found"
- Check requirements.txt includes all packages
- Verify Python version matches (3.8+)

### "Database errors"
- PyQuest uses file storage, no database needed
- Make sure app has write permissions

### "Port binding failed"
- Make sure you're using PORT from environment
- Render/Heroku set this automatically

---

## Next Steps

1. Choose a deployment option
2. Follow the steps above
3. Share your URL with friends!
4. Keep learning Python daily

**Your URL will be something like:**
- `https://pyquest-learning.onrender.com`
- `https://pyquest-learning.herokuapp.com`
- `https://josie.pythonanywhere.com`

Happy deploying! 🚀
