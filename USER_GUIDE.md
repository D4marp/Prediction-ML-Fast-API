# 👥 USER GUIDE
## FastAPI Application - Complete User Manual

---

## 📋 TABLE OF CONTENTS

1. [Getting Started](#getting-started)
2. [Registration](#registration)
3. [Login](#login)
4. [User Management](#user-management)
5. [Item Management](#item-management)
6. [Sales Prediction](#sales-prediction)
7. [Troubleshooting](#troubleshooting)
8. [FAQ](#faq)

---

## 🚀 GETTING STARTED

### System Requirements

**Minimum:**
- Browser: Chrome, Firefox, Safari, or Edge (latest version)
- Internet connection
- No installation needed (web-based)

**For Local Development:**
- Python 3.7+
- 500 MB disk space
- 2 GB RAM

### Accessing the Application

**Online (if deployed):**
```
https://your-domain.com
```

**Local Development:**
```
http://localhost:8000
```

### First Time Setup

1. **Server is running** - Check terminal for "Uvicorn running on..."
2. **Open browser** - Navigate to http://localhost:8000
3. **See welcome page** - Features overview displayed
4. **Ready to use** - No login required initially

---

## 📝 REGISTRATION

### How to Register

**Step 1: Access Register Form**
- Scroll to "📝 Register User" section
- Or click "Register" in navigation

**Step 2: Fill Form Fields**

| Field | Requirements | Example |
|-------|--------------|---------|
| Username | 3-50 chars, alphanumeric | `damar` |
| Email | Valid email format | `damar@gmail.com` |
| Full Name | Optional | `Damar Galih` |
| Password | Min 8 chars | `password123` |

**Step 3: Click "Register" Button**

**Step 4: Wait for Response**
- ✅ Success: "User damar berhasil didaftarkan!"
- ❌ Error: Check message and fix fields

### Registration Rules

**Valid Usernames:**
```
✓ damar, john_doe, user123
✗ damar! (special chars), da (too short), ddd ddd (spaces)
```

**Valid Emails:**
```
✓ user@gmail.com, john.doe@company.co.id
✗ user@, @example.com, user@.com
```

**Valid Passwords:**
```
✓ password123 (8+ chars)
✓ MyPass!@2024 (special chars OK)
✗ pass (too short), 12345678 (no variety recommended)
```

### Validation Errors

| Error | Cause | Solution |
|-------|-------|----------|
| "Username already exists" | Username taken | Choose different username |
| "Invalid email" | Bad format | Use valid email format |
| "User already exists" | Email already registered | Use different email |
| "Validation error" | Missing required field | Fill all required fields |

---

## 🔑 LOGIN

### How to Login

**Step 1: Access Login Form**
- Scroll to "🔑 Login" section
- Or click "Login" in navigation

**Step 2: Enter Credentials**
- Username: Your registered username
- Password: Your password

**Step 3: Click "Login" Button**

**Step 4: Token Received**
- ✅ Token displayed below form
- Token auto-saved in browser
- Can now use authenticated features

### Understanding Tokens

**What is a Token?**
- Secure key that proves you're logged in
- Expires after 30 minutes
- Needed for certain features

**Token Display:**
```
Access Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**What Can You Do With Token?**
- Create/update/delete items
- Use sales prediction
- Access protected endpoints

### Login Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| "Incorrect username or password" | Wrong credentials | Check spelling, try again |
| "User not found" | Username doesn't exist | Register first |
| "Connection refused" | Server not running | Start server |
| "Token expired" | Been > 30 mins | Login again |

---

## 👤 USER MANAGEMENT

### Get User Information

**Purpose:** View details of registered user

**Steps:**
1. Scroll to "👤 Get User" section
2. Enter username in field
3. Click "Get User" button
4. Response shows:
   - Username
   - Email
   - Full Name
   - Account Status

**Example Response:**
```json
{
  "username": "damar",
  "email": "damar@gmail.com",
  "full_name": "Damar Galih",
  "disabled": false
}
```

### User Status

| Status | Meaning | Action |
|--------|---------|--------|
| `disabled: false` | Account active | Can login normally |
| `disabled: true` | Account inactive | Cannot login |

---

## 📦 ITEM MANAGEMENT

### What are Items?

Items = Products you want to manage
- Name: Product name
- Description: Product details
- Price: Product price (Rp)
- Available: In stock or not

### CREATE ITEM

**Purpose:** Add new product to system

**Step 1: Access Form**
- Scroll to "➕ Create Item" section
- Or click "New Item" in menu

**Step 2: Fill Details**

| Field | Example |
|-------|---------|
| Item Name | Laptop Gaming ASUS ROG |
| Description | High-performance laptop with RTX 4090 |
| Price | 25000000 |
| Available | ✓ Checked |

**Step 3: Click "Create Item"**

**Step 4: Success Message**
```
✅ Item "Laptop Gaming ASUS ROG" berhasil dibuat!
```

### Pricing Rules

- Must be greater than 0
- Use Indonesian Rupiah (Rp)
- Examples: 1000000, 15000000, 500000

### Valid Item Names

```
✓ Laptop Gaming
✓ Monitor 4K 27 inch
✓ Keyboard Mechanical RGB

✗ (empty field)
✗ Very very very very very long name exceeding 100 characters limit
```

### VIEW ALL ITEMS

**Purpose:** See all products in system

**How:**
1. Scroll to "📋 All Items" section
2. Click "Load Items" button
3. View all items in list
4. Each item shows:
   - Item ID (copy with icon)
   - Name
   - Description
   - Price
   - Availability status

**Auto-Load:**
Items automatically load when page opens.

**Empty List:**
If no items shown, create one first.

### UPDATE ITEM

**Purpose:** Change item details

**Step 1: Copy Item ID**
- From "All Items" list
- Or remember from create response

**Step 2: Access Update Form**
- Scroll to "✏️ Update/Delete Item" section

**Step 3: Enter Details**
- Item ID: Paste copied ID
- Item Name: New name (optional)
- Price: New price (optional)

**Step 4: Click "Update Item"**

**Step 5: Verify Update**
- Check in items list
- Item now shows new details

### Update Rules

- Can update: name, price
- Leave field empty to keep current value
- Price must be > 0 if provided

**Example:**
```
Item ID: 550e8400-e29b-41d4-a716-446655440000
New Name: Laptop Gaming ASUS ROG Pro
New Price: 26000000
```

### DELETE ITEM

**Purpose:** Remove product from system

**⚠️ Warning:** This action is permanent!

**Step 1: Copy Item ID**
- From "All Items" list

**Step 2: Enter Item ID**
- In Update/Delete section
- Paste Item ID

**Step 3: Click "Delete Item"**

**Step 4: Confirm Delete**
- Dialog appears: "Anda yakin?"
- Click "OK" to confirm
- Item permanently deleted

**Step 5: Verify**
- Check items list
- Item should be gone

---

## 🤖 SALES PREDICTION

### What is Sales Prediction?

Machine Learning model predicts sales based on input features.

**Features = Input Values**
- Can represent: marketing spend, reach, days, etc.
- Numbers separated by commas
- Example: `50.0, 100.0, 25.5`

### How to Use Prediction

**Important:** Must be logged in first!

**Step 1: Login**
- Complete login process
- Get access token

**Step 2: Access Prediction**
- Scroll to "🤖 Sales Prediction" section

**Step 3: Enter Features**
- Format: Numbers separated by commas
- Example: `50.0, 100.0, 25.5`
- Or: `1000, 5000` (2 features)
- Or: `100` (1 feature)

**Step 4: Click "Predict Sales"**

**Step 5: View Result**
- Shows input features
- Shows predicted sales
- Example: `predicted_sales: 241.5`

### Understanding Results

**Example 1:**
```
Features: [50.0, 100.0, 25.5]
Predicted Sales: 241.5
```
Interpretation: Based on inputs, estimated sales = 241.5

**Example 2:**
```
Features: [1000, 2000]
Predicted Sales: 4500
```
Interpretation: Based on marketing spend and reach, sales = 4500

### Prediction Rules

- Must be logged in
- Features must be numbers
- Separated by commas
- Can use decimal (50.5) or integer (50)
- Minimum 1 feature, no maximum

### Common Errors

| Error | Fix |
|-------|-----|
| "Not authenticated" | Login first |
| "Invalid features" | Use numbers only, separated by commas |
| "Missing token" | Login and get token |
| "Invalid input" | Check comma placement |

---

## ⚠️ TROUBLESHOOTING

### General Issues

#### "Connection refused"
**Cause:** Server not running

**Solution:**
1. Open terminal
2. Run: `uvicorn app.main:app --reload`
3. Wait for "Uvicorn running on..."
4. Refresh browser

#### Page not loading
**Cause:** Browser/server issue

**Solution:**
1. Hard refresh: `Cmd + Shift + R` (Mac) or `Ctrl + Shift + F5` (Windows)
2. Try incognito mode
3. Try different browser

#### "Error: Failed to fetch"
**Cause:** Network or CORS issue

**Solution:**
1. Check server is running
2. Check URL is correct
3. Check firewall settings
4. Try localhost instead of 127.0.0.1

### Account Issues

#### "Username already exists"
**Cause:** Username taken

**Solution:**
- Choose different username
- Or login with existing account

#### "Incorrect username or password"
**Cause:** Wrong credentials

**Solution:**
- Check username spelling
- Check password spelling
- Caps lock? Try again
- Forgot password? Note: No recovery available yet

#### "Token expired"
**Cause:** Logged in > 30 minutes ago

**Solution:**
- Login again
- Token refreshes on new login

### Item Issues

#### Item not showing in list
**Cause:** Not created yet or reload needed

**Solution:**
1. Create item first
2. Click "Load Items" to refresh
3. Try page reload

#### Cannot update/delete item
**Cause:** Invalid ID or item not found

**Solution:**
1. Copy exact ID from list
2. Check for typos
3. Item might be already deleted

### Prediction Issues

#### "Predicted sales show 0"
**Cause:** Unusual input or model behavior

**Solution:**
1. Try different feature values
2. Check calculation manually
3. Contact support if persists

#### Cannot access prediction
**Cause:** Not logged in

**Solution:**
1. Login with credentials
2. Ensure token is valid
3. Try login again

---

## ❓ FAQ

### Accounts & Authentication

**Q: How long does token last?**
A: 30 minutes. Login again when expired.

**Q: Can I change password?**
A: Not in current version. Contact admin for reset.

**Q: Can I delete my account?**
A: Not in current version. Contact admin.

**Q: What if I forget username/password?**
A: Contact administrator. No self-recovery available.

### Items & Products

**Q: Maximum items I can create?**
A: Unlimited (depends on database storage).

**Q: Can I see items without login?**
A: Yes, view items anytime. Create/edit needs login.

**Q: Can I bulk upload items?**
A: Not in current version. Use API endpoint for bulk.

**Q: Where is item history?**
A: Not tracked in current version.

### Sales Prediction

**Q: How accurate is prediction?**
A: Based on trained ML model. Accuracy depends on input data.

**Q: Can I use decimal numbers?**
A: Yes, e.g., `50.5, 100.25, 25.0`

**Q: What do features represent?**
A: Customizable per your use case. Could be marketing spend, reach, days, etc.

**Q: Can I see prediction history?**
A: Not in current version.

### Technical

**Q: What browser should I use?**
A: Chrome, Firefox, Safari, Edge (latest recommended).

**Q: Do I need install anything?**
A: Web-based - just need browser. For development - need Python.

**Q: Can I use on mobile?**
A: Yes, responsive design supports mobile.

**Q: Is data encrypted?**
A: Passwords hashed with bcrypt. Use HTTPS in production.

**Q: Can I share tokens?**
A: Not recommended - personal token like password.

### Support

**Q: How to report bugs?**
A: Open issue on GitHub repository.

**Q: How to request features?**
A: GitHub Issues or contact developer.

**Q: Where to get documentation?**
A: GitHub repository or `/docs` endpoint.

**Q: Is there API documentation?**
A: Yes - http://localhost:8000/docs (Swagger UI).

---

## 💡 TIPS & TRICKS

### Productivity Tips

1. **Copy Item IDs Easily**
   - Hover over Item ID card
   - Click copy icon
   - Paste into update/delete form

2. **Reuse Token**
   - Login once
   - Token auto-saved
   - Use predictions without re-login (30 mins)

3. **Keyboard Shortcuts**
   - Tab: Navigate between fields
   - Enter: Submit form
   - Cmd/Ctrl + A: Select all (for IDs)

4. **Faster Item Creation**
   - Keep tab open
   - Create multiple items quickly
   - Items auto-load after each create

### Data Management Tips

1. **Organize Items**
   - Use naming convention: `Category - Name`
   - Example: `Laptop - ASUS ROG Gaming`

2. **Pricing**
   - Use consistent format
   - Round numbers: 10000000 (1M Rp)
   - Easier to track

3. **Backup**
   - Regularly export data
   - Note important item IDs
   - Keep screenshot of items list

### Security Tips

1. **Token Safety**
   - Token never share with others
   - Treat like password
   - Auto-stored, auto-used

2. **Password Tips**
   - Use strong password
   - Mix uppercase, lowercase, numbers
   - Different from other accounts

3. **Browser Tips**
   - Use incognito for testing
   - Clear browser cache if issues
   - Logout when done (clear localStorage)

---

## 📞 GETTING HELP

### Support Channels

1. **GitHub Issues**
   - Report bugs
   - Request features
   - See existing issues

2. **Documentation**
   - `/docs` - Swagger UI
   - `TECHNICAL_DOCUMENTATION.md`
   - `README.md`

3. **Video Tutorial**
   - See VIDEO_DOCUMENTATION.md
   - Step-by-step walkthrough

### What Info to Provide When Asking Help

- Error message (exact text)
- Steps to reproduce
- Browser & version
- Screenshots if possible
- Server version

---

## 📚 ADDITIONAL RESOURCES

### Links

- **FastAPI Docs**: https://fastapi.tiangolo.com
- **SQLAlchemy**: https://www.sqlalchemy.org
- **JWT Info**: https://jwt.io
- **REST API Guide**: https://restfulapi.net

### Related Documentation

- `README.md` - Project overview
- `TECHNICAL_DOCUMENTATION.md` - For developers
- `VIDEO_DOCUMENTATION.md` - Video guide
- `INTEGRATION_GUIDE.md` - Integration details

---

**Happy Using! 🎉**

For more help, check GitHub Issues or contact maintainer.
