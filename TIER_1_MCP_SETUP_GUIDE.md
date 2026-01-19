# Tier 1 MCP Setup Guide
**Date:** January 17, 2026  
**Time:** 21:43 PST  
**Project:** Walk This Way + COMPASS Advanced System  
**Purpose:** Setup instructions for Tier 1 MCPs (Knowledge Graph Memory, Firecrawl, Pandoc, Vectara)

---

## 🎯 TIER 1 MCPS TO ADD

1. ✅ **Knowledge Graph Memory MCP** - Persistent memory for character consistency
2. ✅ **Firecrawl MCP** - Web scraping and deep research
3. ✅ **Pandoc MCP** - Document conversion (Markdown → DOCX, PDF, etc.)
4. ✅ **Vectara MCP** - Semantic search across documents

---

## 📋 SETUP REQUIREMENTS

### **Before Adding MCPs:**

**For Firecrawl MCP:**
- ⚠️ **API Key Required:** Sign up at [firecrawl.dev](https://firecrawl.dev) to get API key
- ⚠️ **Set Environment Variable:** `FIRECRAWL_API_KEY` in your environment

**For Vectara MCP:**
- ⚠️ **API Key Required:** Sign up at [vectara.com](https://vectara.com) to get API key
- ⚠️ **Set Environment Variable:** `VECTARA_API_KEY` and `VECTARA_ENV` in your environment

**For Pandoc MCP:**
- ⚠️ **Pandoc Installed:** Install Pandoc on your system
  - macOS: `brew install pandoc`
  - Or download from [pandoc.org](https://pandoc.org/installing.html)

**For Knowledge Graph Memory MCP:**
- ✅ **No API Key Needed:** Uses local SQLite storage by default
- ✅ **Ready to Use:** Just add to config

---

## 🔧 STEP-BY-STEP SETUP

### **Step 1: Get API Keys (If Needed)**

**Firecrawl:**
1. Visit [firecrawl.dev](https://firecrawl.dev)
2. Sign up for account
3. Get API key from dashboard
4. Set environment variable: `export FIRECRAWL_API_KEY="your-key-here"`

**Vectara:**
1. Visit [vectara.com](https://vectara.com)
2. Sign up for account
3. Get API key and environment ID from dashboard
4. Set environment variables: `export VECTARA_API_KEY="your-key-here"` and `export VECTARA_ENV="your-env-id"`

**Note:** You can add these to your `~/.zshrc` or `~/.bash_profile` to make them permanent.

---

### **Step 2: Install Pandoc (If Needed)**

**macOS:**
```bash
brew install pandoc
```

**Verify Installation:**
```bash
pandoc --version
```

---

### **Step 3: Update MCP Configuration**

The updated `.cursor/config/mcp.json` has been prepared with all Tier 1 MCPs. 

**MCPs Added:**
- `knowledge-graph-memory` - Knowledge Graph Memory MCP
- `firecrawl` - Firecrawl MCP (requires API key)
- `pandoc` - Pandoc MCP (requires Pandoc installed)
- `vectara` - Vectara MCP (requires API key)

**Important:**
- ⚠️ **Firecrawl and Vectara are DISABLED by default** (until API keys are set)
- ✅ **Knowledge Graph Memory and Pandoc are ENABLED** (ready to use)

---

### **Step 4: Enable MCPs (After API Keys)**

**Once you have API keys:**

1. Set environment variables (see Step 1)
2. Edit `.cursor/config/mcp.json`
3. Change `"disabled": true` to `"disabled": false` for Firecrawl and Vectara
4. Restart Cursor completely (Cmd+Q)

---

### **Step 5: Test MCPs**

**After restarting Cursor, test each MCP:**

**Knowledge Graph Memory:**
```
"Store in knowledge graph memory: Nick is 17 years old and loves disco music"
```

**Pandoc:**
```
"Use pandoc to convert my README.md to DOCX format"
```

**Firecrawl (if enabled):**
```
"Use firecrawl to scrape information about 1970s Boston radio stations"
```

**Vectara (if enabled):**
```
"Use vectara to search for similar scenes in my draft about music"
```

---

## ⚠️ TROUBLESHOOTING

### **MCP Not Found:**
- Verify paths in `mcp.json` are correct
- Restart Cursor completely (Cmd+Q, don't just reload)
- Check environment variables are set (for Firecrawl/Vectara)

### **Firecrawl/Vectara Not Working:**
- Check API keys are set: `echo $FIRECRAWL_API_KEY` and `echo $VECTARA_API_KEY`
- Verify API keys are valid (not expired)
- Restart Cursor after setting environment variables

### **Pandoc Not Working:**
- Verify Pandoc is installed: `pandoc --version`
- Check PATH includes Pandoc location
- May need to restart terminal/Cursor after installing Pandoc

### **Knowledge Graph Memory Not Working:**
- Should work without setup (uses SQLite)
- Check for error messages in Cursor MCP logs
- Verify `@modelcontextprotocol/server-memory` package is accessible

---

## 📝 NEXT STEPS

1. ✅ **Get API Keys:** Firecrawl and Vectara (if you want to use them)
2. ✅ **Install Pandoc:** If you want document conversion
3. ✅ **Enable MCPs:** Change `"disabled": false` for Firecrawl/Vectara once keys are set
4. ✅ **Test MCPs:** Try each one to verify they work
5. ✅ **Start Using:** Integrate into your writing workflow!

---

## 🎯 USAGE TIPS

### **Knowledge Graph Memory MCP:**
- Store character traits, plot points, world-building details
- Use for consistency checks across chapters
- Perfect for maintaining character voices

### **Firecrawl MCP:**
- Enable for research mode only
- Great for historical fact-checking
- Use when you need live web content

### **Pandoc MCP:**
- Enable for export mode
- Convert drafts to DOCX for editors
- Generate PDFs for review

### **Vectara MCP:**
- Enable for semantic search across your drafts
- Find similar scenes/themes
- Great for consistency checking

---

*Last Updated: January 17, 2026 21:43 PST*
