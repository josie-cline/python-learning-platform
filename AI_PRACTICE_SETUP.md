# 🤖 AI Practice Challenge Generator Setup

## What Is This?

The **Practice Sandbox** can generate **unlimited unique challenges** using AI!

Instead of recycling curriculum challenges, it creates brand-new problems on-demand based on:
- Topics you select (functions, loops, strings, etc.)
- Difficulty level you choose
- Real-world scenarios

**Every challenge is different!** Practice as much as you want.

---

## 🔑 How to Enable AI Generation

### Step 1: Get an OpenAI API Key

1. **Go to:** https://platform.openai.com/api-keys
2. **Sign in** or create an account
3. Click **"Create new secret key"**
4. **Name it:** `PyQuest Practice Generator`
5. **Copy the key** (starts with `sk-...`)
   - ⚠️ You can only see it once! Save it now.

### Step 2: Add Key to .env File

1. **Open your .env file:**
   ```bash
   cd /Users/josiah.cline/Documents/python-learning-platform
   open .env
   ```

2. **Add this line:**
   ```
   OPENAI_API_KEY=sk-your-actual-key-here
   ```

3. **Save the file** (Cmd + S)

### Step 3: Install OpenAI Package

```bash
pip3 install -r requirements.txt
```

This installs the `openai` package (already in requirements.txt).

### Step 4: Restart Your Server

```bash
# Stop the server (Ctrl + C)
python3 app.py
```

### Step 5: Test It!

1. Go to **http://localhost:5000/practice**
2. Select topics and difficulty
3. Click **"Get Random Challenge"**
4. Watch as AI generates a unique problem!

---

## 💰 Cost Estimate

OpenAI charges per API call:

**GPT-4 pricing (as of 2026):**
- ~$0.01-0.03 per challenge generated
- Generate 100 challenges = $1-3

**Free tier:**
- OpenAI gives $5 free credit to new users
- That's ~200-300 practice challenges free!

**Recommendation:**
- Set a spending limit in OpenAI dashboard
- Start with $5-10/month
- Track usage at https://platform.openai.com/usage

---

## 🎯 What Happens Without API Key?

**Fallback mode:**
- Practice Sandbox uses curriculum challenges
- Randomly selects from Weeks 1-9
- Still works, but challenges repeat
- You'll see a message explaining how to enable AI

---

## ✨ Benefits of AI Generation

**With API key:**
- ✅ Unlimited unique challenges
- ✅ Never see the same problem twice
- ✅ Customized to your selected topics
- ✅ Fresh problems to keep practicing
- ✅ Real-world scenarios

**Without API key:**
- ⚠️ Limited to 63 curriculum challenges
- ⚠️ Same problems repeat
- ✅ Still great for review!

---

## 🔒 Security

**Your API key is safe:**
- Stored in `.env` (never committed to Git)
- Only used locally on your machine
- Not visible in the browser
- Not shared with anyone

---

## 🧪 Test Your Setup

After adding the API key and restarting:

1. **Check console** when server starts - should NOT see errors about OpenAI
2. **Visit Practice page** - should see "✨ Powered by AI" badge
3. **Generate a challenge** - should show loading spinner, then unique problem
4. **Check the problem** - should be different from curriculum

---

## ❓ Troubleshooting

**Error: "API key not valid"**
- Check you copied the entire key (starts with sk-)
- Make sure no extra spaces in .env file
- Verify key is active at https://platform.openai.com/api-keys

**Error: "Rate limit exceeded"**
- You hit OpenAI's limit (too many requests)
- Wait a few minutes
- Upgrade OpenAI plan if needed

**Error: "Insufficient quota"**
- Your OpenAI credits ran out
- Add payment method at https://platform.openai.com/account/billing
- Or wait for monthly reset (free tier)

**Still using curriculum challenges?**
- Check .env file has OPENAI_API_KEY line
- Restart server after adding key
- Check server logs for errors

---

## 💡 Pro Tips

1. **Start without API key** - Practice with curriculum first
2. **Add key later** when you want more variety
3. **Set spending limits** in OpenAI dashboard
4. **Monitor usage** to avoid surprise bills
5. **Free tier lasts a while!** - 200+ challenges free

---

## 🚀 Ready to Generate!

Once you add your API key:
- Every practice challenge is **unique**
- Fresh problems **every time**
- **Infinite** practice potential
- Never run out of material!

Get your API key and start generating! ✨
