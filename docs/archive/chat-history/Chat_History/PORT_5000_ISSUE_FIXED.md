# PORT 5000 ISSUE - FIXED! 🎉
**Created:** January 21, 2026

---

## ⚠️ THE PROBLEM

**Port 5000 is used by Apple's AirPlay Receiver on macOS!**

When you tried to access `http://localhost:5000`, nothing happened because:
- Apple's ControlCenter uses port 5000 for AirPlay
- The cursor-view server couldn't bind to that port
- Browser showed nothing (or connection refused)

---

## ✅ THE SOLUTION

**Use port 5001 instead!**

The cursor-view server supports a `--port` argument to use a different port.

---

## 🚀 HOW TO START THE SERVER

**Run this command:**
```bash
cd /tmp/cursor-view
python3 server.py --port 5001
```

**Then open in your browser:**
```
http://localhost:5001
```

---

## 📋 ALTERNATIVE: DISABLE AIRPLAY RECEIVER

**If you want to use port 5000:**

1. **System Settings** → **General** → **AirDrop & Handoff**
2. **Turn OFF "AirPlay Receiver"**
3. **Then port 5000 will be free**

**But using port 5001 is easier!**

---

## 🎯 QUICK START

**I've started the server on port 5001 for you!**

**Just open:**
```
http://localhost:5001
```

**In Safari or Chrome!**

---

*Issue fixed*  
*HANK - January 21, 2026*
