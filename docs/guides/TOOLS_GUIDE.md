# 🔧 Beginner's Guide to Coding Tools

**Everything you need to know about the tools we're using!**

---

## 🖥️ Terminal / Command Line

### What Is It?
The Terminal (Mac) or Command Prompt (Windows) lets you control your computer using text commands instead of clicking buttons.

### Why Use It?
- Faster for many tasks
- Required for programming
- More powerful than GUI
- Used by all professional developers

### Opening Terminal

**Mac:**
1. Press `Cmd + Space`
2. Type "Terminal"
3. Press Enter

**Windows:**
1. Press `Windows key`
2. Type "cmd" or "PowerShell"
3. Press Enter

### Essential Commands

```bash
# See where you are
pwd
# Output: /Users/josiah.cline/Documents

# List files in current folder
ls
# Output: file1.txt  file2.txt  folder1/

# Change directory (go into a folder)
cd foldername
# Example: cd Documents

# Go up one folder
cd ..

# Go to home folder
cd ~

# Create new folder
mkdir newfolder

# Create new file
touch newfile.txt

# See file contents
cat filename.txt

# Clear screen
clear

# Exit terminal
exit
```

### Tips
- Tab key autocompletes names
- Up arrow shows previous commands
- `Cmd + C` (Mac) or `Ctrl + C` (Windows) stops running programs
- You can copy/paste into Terminal

---

## 🐍 Python

### What Is It?
Python is a programming language - a way to tell computers what to do using human-readable text.

### Why Python?
- Beginner-friendly
- Powerful and versatile
- Used at Google, Netflix, Instagram, Spotify
- Great for web development, AI, data science
- Scale AI uses it!

### Running Python

**Check if installed:**
```bash
python3 --version
```

**Run Python file:**
```bash
python3 myfile.py
```

**Interactive Python (play around):**
```bash
python3
>>> print("Hello!")
Hello!
>>> exit()
```

### Key Concepts

**Variables** - Store data
```python
name = "Josie"
age = 25
```

**Functions** - Reusable code blocks
```python
def greet(name):
    return f"Hello, {name}!"
```

**Loops** - Repeat actions
```python
for i in range(5):
    print(i)  # Prints 0, 1, 2, 3, 4
```

**Conditionals** - Make decisions
```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

## 📦 pip (Python Package Manager)

### What Is It?
pip installs code libraries (packages) that other people wrote, so you don't have to write everything from scratch.

### Why Use It?
- Saves time
- Uses tested, reliable code
- Access to thousands of tools
- Standard in Python development

### Common Commands

```bash
# Install a package
pip3 install flask

# Install from requirements file
pip3 install -r requirements.txt

# List installed packages
pip3 list

# Upgrade a package
pip3 install --upgrade flask

# Uninstall a package
pip3 uninstall flask

# See package info
pip3 show flask
```

### What's requirements.txt?
A file listing all packages your project needs:

```
flask==3.0.0
requests==2.31.0
pyyaml==6.0.1
```

Anyone can install everything at once:
```bash
pip3 install -r requirements.txt
```

---

## 🗂️ Git (Version Control)

### What Is It?
Git tracks changes to your code over time. Think of it as "track changes" for programming.

### Why Use It?
- Save snapshots of your work
- Go back to previous versions
- Collaborate with others
- Required for professional development
- Industry standard

### Key Concepts

**Repository (repo)** - A project folder tracked by Git

**Commit** - A saved snapshot of your code

**Branch** - A separate version to try things

**Remote** - Online copy (like GitHub)

### Essential Commands

```bash
# Initialize Git in a folder
git init

# Check what changed
git status

# Stage files for commit (prepare to save)
git add filename.txt
git add .  # Add all files

# Save a snapshot (commit)
git commit -m "Description of changes"

# See history
git log

# Connect to GitHub
git remote add origin https://github.com/username/repo.git

# Upload to GitHub
git push origin main

# Download from GitHub
git pull origin main

# Clone someone's project
git clone https://github.com/username/repo.git
```

### Typical Workflow

```bash
# 1. Make changes to code
# 2. Check what changed
git status

# 3. Stage changes
git add .

# 4. Commit (save snapshot)
git commit -m "Add new feature"

# 5. Push to GitHub
git push origin main
```

### Tips
- Commit often (multiple times per day)
- Write clear commit messages
- Always pull before pushing
- Don't commit passwords or secrets

---

## 🐙 GitHub

### What Is It?
GitHub is like Google Drive for code. It stores Git repositories online.

### Why Use It?
- Backup your code
- Share with others
- Collaborate on projects
- Portfolio for job hunting
- Free hosting for code

### Key Features

**Repository** - Your project on GitHub

**README** - Description of your project (like a homepage)

**Issues** - Track bugs and todos

**Pull Requests** - Propose changes

**Actions** - Automation (like auto-deploy)

### Getting Started

1. Create account at https://github.com
2. Create new repository
3. Connect local Git to GitHub
4. Push your code

### Connecting Local to GitHub

```bash
# In your project folder
git remote add origin https://github.com/YOUR-USERNAME/repo-name.git
git push -u origin main
```

### Personal Access Token

GitHub now requires tokens instead of passwords:

1. Go to https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Give it a name
4. Select `repo` permissions
5. Click "Generate"
6. Copy the token
7. Use it as your password when pushing

---

## 💻 VS Code (Code Editor)

### What Is It?
VS Code is a text editor designed for writing code. Like Microsoft Word, but for programming.

### Why VS Code?
- Free and open source
- Powerful features
- Extensions for everything
- Used by millions of developers
- Great for beginners

### Download & Install

1. Go to https://code.visualstudio.com
2. Download for your OS
3. Install
4. Open VS Code

### Essential Features

**File Explorer** - Left sidebar, see all files

**Editor** - Middle area, write code

**Terminal** - Bottom panel, run commands

**Extensions** - Add features

### Must-Have Extensions

1. **Python** - Python support
2. **Pylance** - Better Python
3. **Python Debugger** - Find bugs
4. **GitLens** - Better Git
5. **Prettier** - Format code

### Installing Extensions

1. Click Extensions icon (left sidebar)
2. Search for extension name
3. Click "Install"

### Useful Shortcuts

**Mac:**
- `Cmd + S` - Save
- `Cmd + P` - Quick open file
- `Cmd + Shift + P` - Command palette
- `Cmd + /` - Comment/uncomment
- `Cmd + F` - Find
- `Cmd + D` - Select next occurrence

**Windows:**
- Same but `Ctrl` instead of `Cmd`

### Opening Project in VS Code

```bash
cd /path/to/project
code .
```

Or: File > Open Folder

---

## 🌐 Web Browsers (Chrome DevTools)

### What Are DevTools?
Every browser has developer tools for inspecting websites.

### Opening DevTools

**Chrome/Edge:**
- Mac: `Cmd + Option + I`
- Windows: `F12` or `Ctrl + Shift + I`

**Firefox:**
- Mac: `Cmd + Option + I`
- Windows: `F12` or `Ctrl + Shift + I`

### Useful Tabs

**Console** - See errors, run JavaScript

**Elements** - Inspect HTML/CSS

**Network** - See requests/responses

**Application** - See storage, cookies

### For PyQuest

Use Console to see:
- JavaScript errors
- Debugging messages
- Test results

---

## 🔐 Environment Variables (.env file)

### What Are They?
Secret settings that aren't committed to Git (like passwords, API keys).

### Why Use Them?
- Keep secrets secret
- Different settings per environment
- Industry best practice

### .env File Format

```bash
# Comments start with #
USER_NAME=Josie Cline
USER_EMAIL=josiah.cline@scale.com
API_KEY=secret123

# No spaces around =
# No quotes needed (usually)
# Each variable on new line
```

### Loading in Python

```python
from dotenv import load_dotenv
import os

load_dotenv()  # Load .env file

name = os.getenv('USER_NAME')  # Get variable
print(name)  # "Josie Cline"
```

### Security

**ALWAYS:**
- Add `.env` to `.gitignore`
- Never commit secrets
- Use `.env.example` for templates

**Example .gitignore:**
```
.env
*.env.local
```

---

## 🚀 Deployment Platforms

### What Is Deployment?
Putting your app online so others can access it via URL.

### Render.com

**Pros:**
- Free tier
- Easy setup
- Auto-deploys from GitHub
- Good for beginners

**Cons:**
- Free tier sleeps after inactivity
- First load slow

**Best for:** Learning projects

### Heroku

**Pros:**
- Very popular
- Great documentation
- Many add-ons

**Cons:**
- Free tier limited
- Need credit card

**Best for:** Small apps

### PythonAnywhere

**Pros:**
- Python-specific
- Easy for beginners
- Good free tier

**Cons:**
- Limited to Python
- Less flexible

**Best for:** Python learning

---

## 📚 File Formats

### .py - Python Files
Your Python code

### .yaml / .yml - YAML Files
Configuration and data (human-readable)

```yaml
name: Josie
age: 25
skills:
  - Python
  - JavaScript
```

### .json - JSON Files
Data format (like YAML but stricter)

```json
{
  "name": "Josie",
  "age": 25,
  "skills": ["Python", "JavaScript"]
}
```

### .md - Markdown Files
Documentation (like this file!)

```markdown
# Heading
**bold** *italic*
- List item
[Link](url)
```

### .gitignore - Git Ignore
Files Git should ignore

```
# Ignore these
.env
__pycache__/
*.pyc
```

### .html - HTML Files
Web page structure

### .css - CSS Files
Web page styling

### .js - JavaScript Files
Web page behavior

---

## 🎓 Learning Resources

### For Terminal
- https://www.codecademy.com/learn/learn-the-command-line

### For Python
- https://docs.python.org/3/tutorial/
- https://www.learnpython.org/

### For Git
- https://git-scm.com/book/en/v2
- https://learngitbranching.js.org/

### For VS Code
- https://code.visualstudio.com/docs

### General
- https://stackoverflow.com/ (Q&A)
- https://github.com/explore (projects)
- https://dev.to/ (articles)

---

## 💡 Pro Tips

### Terminal
- Use tab to autocomplete
- Use up arrow for previous commands
- Learn 5-10 commands really well

### Python
- Read error messages carefully
- Google "python how to [thing]"
- Practice daily
- Comment your code

### Git
- Commit often
- Write clear messages
- Push daily
- Keep commits small

### VS Code
- Learn shortcuts
- Use extensions
- Customize to your liking
- Use integrated terminal

### Learning
- Be consistent
- Build projects
- Read others' code
- Ask questions
- Share your progress

---

## 🆘 Common Issues

### "Command not found"
- Not installed OR not in PATH
- Install the tool
- Restart terminal

### "Permission denied"
- Need admin rights
- Use `sudo` (Mac/Linux)
- Run as administrator (Windows)

### "Module not found"
- Package not installed
- Run `pip3 install package-name`

### "Port already in use"
- Something running on that port
- Change port OR kill process

### Git merge conflicts
- Edit files to resolve
- Stage resolved files
- Commit

---

## 🎯 Next Steps

1. ✅ Read this guide
2. 📝 Try each tool
3. 🐍 Complete first Python challenge
4. 🔧 Set up VS Code
5. 🐙 Create GitHub account
6. 🚀 Deploy your app

**You've got this!** 🌟

Every professional developer started exactly where you are now. The tools seem overwhelming at first, but you'll be comfortable with them in weeks!

Keep this guide handy - refer back anytime you're confused about a tool.

Happy coding! 🐍
