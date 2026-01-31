# Practice Sandbox Testing Guide

## 🐛 Bug Fixed!

**Issue:** Practice filters weren't working - selecting topics like "functions", "variables", "strings" returned no challenges.

**Root Cause:** Challenges only had descriptive `topic` fields like "Your First Python Program" instead of searchable keywords.

**Fix:** Added `keywords` array to all 28 challenges with proper searchable terms.

---

## 🧪 How to Test

### 1. Start the Server

```bash
cd /Users/josiah.cline/Documents/python-learning-platform
python3 app.py
```

### 2. Open Practice Sandbox

Go to: **http://localhost:5000/practice**

### 3. Test Each Filter

#### Test 1: Functions
- ✅ Check "Functions"
- Click "Get Random Challenge"
- **Expected:** You should see challenges like:
  - Week 1, Day 1: "Hello, World!"
  - Week 3, Day 1: "Function Basics"
  - Week 4, Day 2: "Dictionary Methods"

#### Test 2: Variables
- ✅ Check "Variables"
- Click "Get Random Challenge"
- **Expected:** You should see challenges like:
  - Week 1, Day 2: "Variables and Numbers"
  - Week 2, Day 3: "Count to Ten"

#### Test 3: Strings
- ✅ Check "Strings"
- Click "Get Random Challenge"
- **Expected:** You should see challenges like:
  - Week 1, Day 1: "Hello, World!"
  - Week 1, Day 3: "String Basics"
  - Week 1, Day 6: "String Length and Repeat"

#### Test 4: Loops
- ✅ Check "Loops"
- Click "Get Random Challenge"
- **Expected:** You should see challenges like:
  - Week 2, Day 3: "Count to Ten"
  - Week 2, Day 5: "Sum of List"
  - Week 3, Day 6: "Remove Duplicates"

#### Test 5: Conditions (If/Else)
- ✅ Check "If/Else"
- Click "Get Random Challenge"
- **Expected:** You should see challenges like:
  - Week 2, Day 1: "Even or Odd?"
  - Week 2, Day 2: "Grade Calculator"

#### Test 6: Lists
- ✅ Check "Lists"
- Click "Get Random Challenge"
- **Expected:** You should see challenges like:
  - Week 2, Day 5: "Sum of List"
  - Week 3, Day 3: "List Operations"
  - Week 3, Day 4: "List Slicing"

#### Test 7: Dictionaries
- ✅ Check "Dictionaries"
- Click "Get Random Challenge"
- **Expected:** You should see challenges like:
  - Week 4, Day 1: "Dictionary Basics"
  - Week 4, Day 3: "Word Counter"
  - Week 4, Day 7: "Phonebook"

#### Test 8: Math Operations
- ✅ Check "Math Operations"
- Click "Get Random Challenge"
- **Expected:** You should see challenges like:
  - Week 1, Day 2: "Variables and Numbers"
  - Week 1, Day 4: "Simple Calculator"
  - Week 2, Day 1: "Even or Odd?"

### 4. Test Multiple Filters

- ✅ Check "Loops" + "Lists"
- Click "Get Random Challenge"
- **Expected:** Challenges that use BOTH loops and lists:
  - Week 2, Day 5: "Sum of List"
  - Week 3, Day 6: "Remove Duplicates"

### 5. Test Difficulty Filter

- Select "Beginner"
- ✅ Check "Functions"
- Click "Get Random Challenge"
- **Expected:** Only beginner-level function challenges

---

## ✅ All Keywords by Week

### Week 1 (Python Basics)
- Day 1: functions, strings
- Day 2: variables, math
- Day 3: strings, variables
- Day 4: math, variables
- Day 5: strings, variables, functions, math
- Day 6: strings, variables
- Day 7: variables, strings, math, functions

### Week 2 (Control Flow)
- Day 1: conditions, math
- Day 2: conditions, math
- Day 3: loops, variables
- Day 4: loops, conditions, math
- Day 5: loops, lists, math
- Day 6: loops, lists, conditions
- Day 7: loops, conditions, strings

### Week 3 (Functions & Lists)
- Day 1: functions
- Day 2: functions
- Day 3: lists, functions
- Day 4: lists
- Day 5: lists, functions
- Day 6: lists, loops
- Day 7: lists, functions, loops, math

### Week 4 (Dictionaries & Sets)
- Day 1: dictionaries
- Day 2: dictionaries, functions
- Day 3: dictionaries, loops, strings
- Day 4: dictionaries, functions
- Day 5: lists
- Day 6: lists, functions
- Day 7: dictionaries, functions, loops

---

## 🎯 Success Criteria

✅ Each topic filter returns relevant challenges  
✅ Multiple filters work together (AND logic)  
✅ Difficulty filter works correctly  
✅ "Get Random Challenge" with no filters shows any challenge  
✅ No "No challenges found" errors when valid filters are selected  

---

## 🚨 If You Still Have Issues

1. **Restart the server:**
   - Press `Ctrl + C` to stop
   - Run `python3 app.py` again

2. **Check browser console:**
   - Right-click → Inspect → Console tab
   - Look for any JavaScript errors

3. **Try clearing cache:**
   - Hard refresh: `Cmd + Shift + R` (Mac) or `Ctrl + Shift + R` (Windows/Linux)
