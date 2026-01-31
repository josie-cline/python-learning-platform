# 🧪 Testing PyQuest - Quick Test Guide

## ✅ What We're Testing

1. Application starts successfully
2. Homepage loads
3. Week 1, Day 1 challenge loads with new teaching content
4. Code editor works
5. Test runner works
6. Navigation works

## 🚀 How to Test (5 Minutes)

### Step 1: Start the Server

```bash
cd /Users/josiah.cline/Documents/python-learning-platform
python3 app.py
```

**Expected:** You should see the PyQuest banner with "Open your browser to: http://localhost:5000"

### Step 2: Open in Browser

Open: **http://localhost:5000**

**Expected:** 
- ✅ Homepage loads
- ✅ You see your name (from .env file)
- ✅ Stats show (might be 0 if first time)
- ✅ "Today's Challenge" card appears

### Step 3: Test Today's Challenge

Click **"Today's Challenge"** or **"Start Challenge"** button

**Expected:**
- ✅ Challenge page loads
- ✅ Left side shows instructions
- ✅ **NEW:** You should see "🎓 LESSON" section with teaching content!
- ✅ Right side shows code editor
- ✅ Starter code is pre-filled

### Step 4: Test the Code Editor

In the code editor, replace the starter code with:

```python
def hello_world():
    print("Hello, World!")
```

Click **"Run Tests"**

**Expected:**
- ✅ Test results appear
- ✅ Shows if tests passed or failed
- ✅ If passed: Green success message!

### Step 5: Test Navigation

Click through the nav bar:
- **Dashboard** - Should go back to homepage
- **Curriculum** - Should show 6-month roadmap
- **Progress** - Should show your progress (might be empty)
- **Resources** - Should show learning resources with clickable links

### Step 6: Stop the Server

In Terminal, press **Ctrl + C**

**Expected:** Server stops

## 🎯 What to Check Specifically

### New Teaching Content
When you open Week 1, Day 1 challenge, you should see:

1. **Lesson Section** with:
   - "What You'll Learn"
   - "Part 1: The print() Function"
   - "Part 2: Strings (Text)"
   - "Part 3: Functions"
   - Multiple code examples
   - Explanations of each concept

2. **Instructions** that are:
   - Step-by-step
   - Clear and detailed
   - Show the expected solution

3. **Starter Code** with:
   - Helpful comments
   - Guidance on what to do

## 🐛 Common Issues & Fixes

### "Module not found"
```bash
pip3 install -r requirements.txt
```

### "Port 5000 already in use"
Edit `.env` and change `PORT=5000` to `PORT=5001`

### Page won't load
- Check server is running (should see logs in Terminal)
- Try http://127.0.0.1:5000 instead
- Check for errors in Terminal

### Tests won't run
- Check browser console (F12) for JavaScript errors
- Make sure code has no syntax errors
- Verify starter code matches expected format

## ✅ Success Checklist

After testing, you should have verified:

- [ ] Server starts without errors
- [ ] Homepage loads with all sections
- [ ] Navigation works (all pages load)
- [ ] Challenge page shows new teaching content
- [ ] Code editor is editable
- [ ] Can run tests successfully
- [ ] Test results display correctly
- [ ] Links in Resources page are clickable
- [ ] No console errors (F12 in browser)

## 📊 What's Ready

**Production Ready:**
- ✅ Week 1 (7 challenges) - Full teaching content
- ✅ Week 2 (7 challenges) - Full teaching content
- ✅ Week 3, Day 1 - Full teaching content

**Available but needs teaching:**
- ⚠️ Week 3, Days 2-7
- ⚠️ Week 4, All days

**Recommendation:** Start with Week 1, Day 1 and work through Week 2. By then, we'll have updated the rest!

## 🎉 If Everything Works

You're ready to start learning Python! 

Next steps:
1. Complete `.env` setup if you haven't
2. Set up GitHub (see GITHUB_DEPLOYMENT_GUIDE.md)
3. Deploy to Render to get your URL
4. Start Week 1, Day 1!

## 📞 If Something Doesn't Work

1. Check Terminal for error messages
2. Check browser console (F12) for errors
3. Verify you're in the right directory
4. Make sure all files are present
5. Try restarting the server

---

**Happy Testing!** 🐍🚀

If tests pass, you have a fully functional Python learning platform with comprehensive teaching content for the first 2 weeks!
