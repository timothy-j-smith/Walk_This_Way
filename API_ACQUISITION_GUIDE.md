# API ACQUISITION GUIDE
## Step-by-Step Team Process
**Date:** January 24, 2026  
**Status:** 🚀 **READY TO START**

---

## WHY YOU NEED A SEPARATE ANTHROPIC API KEY

### **Current Situation:**
- ✅ You have Claude through Cursor (Ultra Plan)
- ⚠️ But your **custom MCPs need direct API access**

### **MCPs That Require Anthropic API Key:**
1. **Style Emulation MCP** - Needs API for style transformation
2. **ZEN Orchestrator MCP** - Needs API to route to Claude via API (not just Cursor)

### **Benefits of Separate API Key:**
- ✅ **Unlimited Usage** - No Cursor plan limits
- ✅ **Direct MCP Access** - Custom MCPs can use Claude directly
- ✅ **Better Control** - Track usage, set budgets
- ✅ **ZEN Integration** - ZEN can route to Claude via API
- ✅ **COMPASS Premium** - Enables full multi-model orchestration

### **Cost Estimate:**
- Cursor Ultra: ~$40/month (you're already paying)
- Anthropic API: ~$20-40/month (based on usage)
- **Total:** Similar or slightly more, but **unlimited usage**

**Verdict:** ✅ **YES, GET IT** - Essential for COMPASS Premium and custom MCPs

---

## API ACQUISITION CHECKLIST

### **Priority 1: Critical APIs (For COMPASS Premium)**

#### **1. Anthropic API Key** ⭐⭐⭐⭐⭐
**Status:** ⚠️ **NEEDED**  
**Used By:** Style Emulation MCP, ZEN MCP  
**Why Critical:** Enables custom MCPs and multi-model orchestration

**Steps:**
1. Go to <https://console.anthropic.com/>
2. Sign up or log in
3. Navigate to "API Keys"
4. Click "Create Key"
5. Name it: "COMPASS Premium - Walk This Way"
6. Copy the key (starts with `sk-ant-...`)
7. **DO NOT SHARE** - Keep it secret!

**Cost:** Pay-per-use (~$20-40/month estimated)

---

#### **2. OpenAI API Key** ⭐⭐⭐⭐⭐
**Status:** ⚠️ **NEEDED**  
**Used By:** ZEN MCP (for GPT-4 dialogue generation)  
**Why Critical:** Enables multi-model orchestration (Premium Feature 6)

**Steps:**
1. Go to <https://platform.openai.com/>
2. Sign up or log in
3. Navigate to "API Keys"
4. Click "Create new secret key"
5. Name it: "COMPASS Premium - ZEN MCP"
6. Copy the key (starts with `sk-...`)
7. **DO NOT SHARE** - Keep it secret!

**Cost:** Pay-per-use (~$10-30/month estimated for GPT-4 usage)

---

#### **3. Google API Key** ⭐⭐⭐⭐⭐
**Status:** ⚠️ **NEEDED**  
**Used By:** ZEN MCP (for Gemini analysis)  
**Why Critical:** Enables multi-model orchestration (Premium Feature 6)

**Steps:**
1. Go to <https://ai.google.dev/>
2. Sign up or log in
3. Navigate to "Get API Key"
4. Create new API key
5. Name it: "COMPASS Premium - ZEN MCP"
6. Copy the key
7. **DO NOT SHARE** - Keep it secret!

**Cost:** Free tier available, then pay-per-use

---

#### **4. Firecrawl API Key** ⭐⭐⭐⭐⭐
**Status:** ⚠️ **NEEDED**  
**Used By:** Firecrawl MCP (PRIMARY research tool)  
**Why Critical:** Enables comprehensive research (Premium Feature 9)

**Steps:**
1. Go to <https://firecrawl.dev/>
2. Sign up or log in
3. Navigate to "API Keys" or "Settings"
4. Create new API key
5. Name it: "COMPASS Premium - Research"
6. Copy the key
7. **DO NOT SHARE** - Keep it secret!

**Cost:** Check pricing (likely paid, but may have free tier)

---

#### **5. Vectara API Key** ⭐⭐⭐⭐⭐
**Status:** ⚠️ **NEEDED**  
**Used By:** Vectara MCP (semantic search)  
**Why Critical:** Enables semantic search and RAG (Premium Feature 9)

**Steps:**
1. Go to <https://vectara.com/>
2. Sign up (free tier available)
3. Create a "Corpus" (this is your environment)
4. Navigate to "API Keys"
5. Create new API key
6. Copy the key
7. **Also get:** Environment ID (from Corpus settings)
8. **DO NOT SHARE** - Keep it secret!

**Cost:** Free tier available, then pay-per-use

---

### **Priority 2: Optional APIs**

#### **6. n8n API Key** ⭐⭐⭐
**Status:** ⏳ **OPTIONAL**  
**Used By:** n8n MCP (workflow automation)  
**Why Optional:** Only needed if you want workflow automation

**Steps:**
1. **Option A: Self-Hosted (Free)**
   - Install n8n locally
   - Get API key from local instance
   
2. **Option B: Cloud (Paid)**
   - Sign up at <https://n8n.io/>
   - Get API key from cloud instance

**Cost:** Free (self-hosted) or paid (cloud)

---

## ENVIRONMENT VARIABLE SETUP

### **Where to Store API Keys:**

**Option 1: Cursor Environment Variables (Recommended)**
- Cursor automatically reads `env:VARIABLE_NAME` from your system
- Set in your shell profile (`.zshrc` or `.bash_profile`)

**Option 2: Direct in mcp.json (Not Recommended)**
- Less secure
- Harder to manage

### **How to Set Environment Variables:**

#### **For macOS (zsh):**
1. Open Terminal
2. Edit your `.zshrc` file:
   ```bash
   nano ~/.zshrc
   ```
3. Add your API keys:
   ```bash
   export ANTHROPIC_API_KEY="sk-ant-your-key-here"
   export OPENAI_API_KEY="sk-your-key-here"
   export GOOGLE_API_KEY="your-key-here"
   export FIRECRAWL_API_KEY="your-key-here"
   export VECTARA_API_KEY="your-key-here"
   export VECTARA_ENV="your-environment-id-here"
   export N8N_API_KEY="your-key-here"  # Optional
   ```
4. Save and exit (Ctrl+X, then Y, then Enter)
5. Reload your shell:
   ```bash
   source ~/.zshrc
   ```

#### **Verify Environment Variables:**
```bash
echo $ANTHROPIC_API_KEY
echo $OPENAI_API_KEY
echo $GOOGLE_API_KEY
echo $FIRECRAWL_API_KEY
echo $VECTARA_API_KEY
echo $VECTARA_ENV
```

**If you see the keys, you're good!**

---

## TESTING EACH API

### **After Setting Up Each API:**

#### **1. Test Anthropic API:**
```bash
# Test in terminal
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{"model": "claude-3-5-sonnet-20241022", "max_tokens": 10, "messages": [{"role": "user", "content": "Hello"}]}'
```

**Expected:** JSON response with message content

---

#### **2. Test OpenAI API:**
```bash
# Test in terminal
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer $OPENAI_API_KEY"
```

**Expected:** List of available models

---

#### **3. Test Google API:**
```bash
# Test in terminal (if available)
# Check Google AI documentation for test command
```

---

#### **4. Test Firecrawl API:**
```bash
# Test in terminal
curl -X POST https://api.firecrawl.dev/v0/scrape \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'
```

**Expected:** JSON response with scraped content

---

#### **5. Test Vectara API:**
```bash
# Test in terminal
curl -X POST "https://api.vectara.io/v1/query" \
  -H "x-api-key: $VECTARA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "test", "corpusKey": ["'$VECTARA_ENV'"]}'
```

**Expected:** JSON response with search results

---

## VERIFY IN CURSOR

### **After Setting Up All APIs:**

1. **Restart Cursor** (to load environment variables)

2. **Check MCP Configuration:**
   - Open `.cursor/config/mcp.json`
   - Verify all `env:VARIABLE_NAME` references are correct

3. **Test MCPs:**
   - Try using Style Emulation MCP
   - Try using ZEN MCP
   - Try using Firecrawl MCP
   - Try using Vectara MCP

4. **Check for Errors:**
   - Look for API key errors in Cursor
   - Check MCP server logs
   - Verify environment variables are loaded

---

## COST TRACKING

### **Estimated Monthly Costs:**

| API | Estimated Cost | Notes |
|-----|---------------|-------|
| Anthropic | $20-40 | Based on usage |
| OpenAI | $10-30 | GPT-4 usage |
| Google | $0-20 | Free tier available |
| Firecrawl | $? | Check pricing |
| Vectara | $0-20 | Free tier available |
| **Total** | **$30-110/month** | Varies by usage |

### **Cost Optimization:**
- Use free tiers where available (Google, Vectara)
- Monitor usage in each API dashboard
- Set budget alerts
- Optimize MCP usage to reduce API calls

---

## SECURITY BEST PRACTICES

### **DO:**
- ✅ Store API keys in environment variables
- ✅ Use `env:VARIABLE_NAME` in mcp.json
- ✅ Never commit API keys to Git
- ✅ Rotate keys periodically
- ✅ Use different keys for different projects

### **DON'T:**
- ❌ Hardcode API keys in files
- ❌ Share API keys publicly
- ❌ Commit keys to Git repositories
- ❌ Use same key for multiple projects

---

## TROUBLESHOOTING

### **Problem: API key not working**
**Solution:**
1. Verify key is correct (no extra spaces)
2. Check environment variable is set: `echo $VARIABLE_NAME`
3. Restart Cursor
4. Check API key hasn't expired
5. Verify API key has correct permissions

### **Problem: MCP not connecting**
**Solution:**
1. Check MCP configuration in `.cursor/config/mcp.json`
2. Verify environment variable name matches
3. Check MCP server logs
4. Restart Cursor

### **Problem: High API costs**
**Solution:**
1. Monitor usage in API dashboards
2. Set budget alerts
3. Optimize MCP usage
4. Use free tiers where available

---

## NEXT STEPS

### **After Securing All APIs:**

1. ✅ **Verify All APIs Work**
   - Test each API
   - Verify in Cursor
   - Check for errors

2. ✅ **Update Documentation**
   - Document API setup
   - Note any issues
   - Update cost tracking

3. ✅ **Proceed to Phase 2**
   - Complete Memory System testing
   - Integrate MCPs into COMPASS Premium
   - Follow roadmap

---

**Status:** 🚀 **READY TO START**  
**Next:** Let's secure APIs one by one, starting with Anthropic!
