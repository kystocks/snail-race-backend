# CORS Security Update - Deployment Checklist

## What Changed Locally ✅

Updated `/snailrace/settings.py`:
- ✅ Removed `CORS_ALLOW_ALL_ORIGINS = True` (security risk)
- ✅ Added specific allowed origins:
  - `https://kystocks.github.io` (production frontend)
  - `http://localhost:5173` (development)
  - `http://127.0.0.1:5173` (development alternative)

## Local Testing

Your local development should continue working as before because we explicitly allowed `localhost:5173`.

**Test it:**
1. Start backend: `python manage.py runserver`
2. Start frontend: `npm run dev`
3. Play a race and verify saves work

## PythonAnywhere Action Required

You need to verify your production settings on PythonAnywhere also have proper CORS configuration.

**Check on PythonAnywhere:**

1. Open Bash console on PythonAnywhere

2. View your production settings:
   ```bash
   cat ~/snail-race-backend/snailrace/settings_production.py | grep -A5 CORS
   ```

3. It should have:
   ```python
   CORS_ALLOWED_ORIGINS = [
       'https://kystocks.github.io',
   ]
   ```

4. It should **NOT** have:
   ```python
   CORS_ALLOW_ALL_ORIGINS = True  # BAD - remove this!
   ```

If your production settings have `CORS_ALLOW_ALL_ORIGINS = True`, update it:

```bash
cd ~/snail-race-backend/snailrace
nano settings_production.py
```

Find the CORS section and change it to:
```python
# CORS for production - only allow GitHub Pages
CORS_ALLOWED_ORIGINS = [
    'https://kystocks.github.io',
]
```

Then reload your web app in the PythonAnywhere Web tab.

## Why This Matters

**Before (Insecure):**
- ANY website could call your API
- Malicious sites could spam your database
- No protection against abuse

**After (Secure):**
- Only your frontend and localhost can call API
- Protected against unauthorized access
- Industry-standard security practice

## Summary

✅ **Local (settings.py):** Fixed - specific origins only
⚠️ **Production (settings_production.py):** Check and update if needed
✅ **Development:** Still works with localhost allowed
✅ **Production frontend:** Still works with GitHub Pages allowed
