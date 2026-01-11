# Fix "command not found: gk"
**Date:** January 10, 2026

---

## PROBLEM

You ran `gk auth login` but got:
```
zsh: command not found: gk
```

---

## CAUSE

We added `~/.local/bin` to your PATH in `~/.zshrc`, but your current terminal session hasn't reloaded it yet.

---

## SOLUTION

**Option 1: Reload your shell configuration (EASIEST)**

In your terminal, run:
```bash
source ~/.zshrc
```

Then try:
```bash
gk --version
gk auth login
```

---

**Option 2: Open a new terminal window**

Just open a fresh terminal window/tab, and `gk` should work automatically.

---

**Option 3: Use the full path (temporary)**

```bash
~/.local/bin/gk auth login
```

---

**Try Option 1 first - just run `source ~/.zshrc` in your terminal!**
