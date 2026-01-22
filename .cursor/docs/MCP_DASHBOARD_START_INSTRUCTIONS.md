# MCP DASHBOARD - HOW TO START (SUPER SIMPLE!)
**Created:** January 21, 2026

---

## 🎯 WHAT YOU NEED TO DO

**You need TWO terminal windows open at the same time:**
- **Window 1:** Runs the backend server (the data)
- **Window 2:** Runs the frontend server (the website)

**Both must be running at the same time!**

---

## 📋 STEP-BY-STEP INSTRUCTIONS

### **STEP 1: Open Your First Terminal Window**

**On Mac:**
- Press `Command + Space` (opens Spotlight)
- Type: `Terminal`
- Press `Enter`

**OR:**
- Go to Applications → Utilities → Terminal

---

### **STEP 2: In Terminal Window 1, Type This:**

```bash
cd /tmp/mcp-dashboard/backend && python3 server.py
```

**Press Enter**

**You should see:**
```
 * Running on http://127.0.0.1:5002
```

**✅ GOOD! Leave this window open! Don't close it!**

---

### **STEP 3: Open a SECOND Terminal Window**

**On Mac:**
- Press `Command + T` in your existing Terminal window
- **OR** Press `Command + N` to open a new window
- **OR** Go to Applications → Utilities → Terminal again

**You now have TWO terminal windows open!**

---

### **STEP 4: In Terminal Window 2, Type This:**

```bash
cd /tmp/mcp-dashboard/frontend && npm install && npm start
```

**Press Enter**

**This will:**
1. Install dependencies (takes a minute)
2. Start the frontend server
3. **Automatically open your browser!** 🎉

**You should see:**
```
Compiled successfully!

You can now view mcp-dashboard in the browser.

  Local:            http://localhost:3000
```

**✅ Your browser should open automatically!**

---

## 🎉 THAT'S IT!

**You should now see the MCP Dashboard in your browser!**

---

## ⚠️ IMPORTANT NOTES

### **Both Windows Must Stay Open!**

- **Window 1** (backend) must keep running
- **Window 2** (frontend) must keep running
- **Don't close either window!**

### **To Stop the Dashboard:**

1. Go to **Window 1** (backend)
2. Press `Control + C` (stops the server)
3. Go to **Window 2** (frontend)
4. Press `Control + C` (stops the server)

---

## 🆘 TROUBLESHOOTING

### **If npm install fails:**

```bash
# Make sure you have Node.js installed
node --version

# If not installed:
brew install node
```

### **If python3 server.py fails:**

```bash
# Make sure you have Flask installed
pip3 install flask flask-cors

# Then try again:
cd /tmp/mcp-dashboard/backend && python3 server.py
```

### **If browser doesn't open:**

**Just go to:** `http://localhost:3000` in your browser manually!

---

## 📸 VISUAL GUIDE

```
┌─────────────────────────────────────┐
│   TERMINAL WINDOW 1 (Backend)        │
│   ─────────────────────────────      │
│   $ cd /tmp/mcp-dashboard/backend    │
│   $ python3 server.py                │
│   * Running on http://127.0.0.1:5002 │
│   (Leave this running!)              │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│   TERMINAL WINDOW 2 (Frontend)      │
│   ─────────────────────────────      │
│   $ cd /tmp/mcp-dashboard/frontend   │
│   $ npm install && npm start         │
│   Compiled successfully!             │
│   Local: http://localhost:3000       │
│   (Browser opens automatically!)     │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│   YOUR BROWSER                       │
│   ─────────────────────────────      │
│   http://localhost:3000              │
│   (MCP Dashboard appears here!)      │
└─────────────────────────────────────┘
```

---

## ✅ QUICK CHECKLIST

- [ ] Terminal Window 1 open
- [ ] Backend running (Window 1)
- [ ] Terminal Window 2 open
- [ ] Frontend running (Window 2)
- [ ] Browser opened automatically
- [ ] Dashboard visible!

---

**That's it! Super simple!** 🚀

*Step-by-step instructions*  
*HANK - January 21, 2026*
