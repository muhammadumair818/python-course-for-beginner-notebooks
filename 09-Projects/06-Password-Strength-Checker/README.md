# Password Strength Checker

Evaluate password security and get recommendations.

## Features

- ✅ Check character variety
- 📏 Verify minimum length
- 🚫 Detect weak patterns
- 🔐 Generate strength score
- 💡 Provide improvement tips

## How to Run

```bash
python checker.py
```

## Menu Options

1. **Check Password** - Analyze a password
2. **Password Tips** - Security guidelines
3. **Exit** - Quit

## Strength Criteria

A strong password should have:
- ✅ 12+ characters
- ✅ Uppercase letters (A-Z)
- ✅ Lowercase letters (a-z)
- ✅ Numbers (0-9)
- ✅ Special characters (!@#$%)

## Sample Output

```
Enter password to check: MyPassword123!

Password: **************
Strength: 🔒 STRONG
Score: 5/6

Feedback:
  ✅ Strong password!
  ⚠️ Consider using 12+ characters
```

## Security Tips

⚠️ **Don't do this:**
- ❌ password123
- ❌ admin
- ❌ 123456
- ❌ qwerty
- ❌ Your name or birthday

✅ **Do this instead:**
- Use random combinations
- Mix character types
- Use unique passwords per site
- Consider a password manager

## Learning Concepts

- Regular expressions (regex)
- String validation
- Pattern matching
- User input handling
- Conditional logic

---

Stay secure! 🔐
