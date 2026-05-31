# 📧 Email Automation — Personalized Outreach from Excel

## 💼 The Problem
Sending personalized emails one by one is slow, inconsistent, and
doesn't scale. A business with 200 customers can't manually type
each name, copy-paste each email address, and hit send 200 times.

This script eliminates that entirely — load a contact list, run
the script, done.

---

## ✅ What it solves
| Problem | Fix Applied |
|---|---|
| Manual copy-pasting emails | Reads contacts automatically from Excel |
| Generic "Dear Customer" emails | Personalizes each email with first name |
| One bad email crashing everything | Each send wrapped in error handling |
| Hardcoded credentials in code | Loaded securely from .env file |

---

## 🛠 Tech Stack
- Python 3.x
- OpenPyXL
- smtplib (built-in)
- python-dotenv

---

## ▶️ How to run

# 1. Install dependencies
pip install -r requirements.txt

# 2. Create a .env file with your credentials
EMAIL_ADDRESS=yourgmail@gmail.com
EMAIL_PASSWORD=your16charapppassword

# 3. Add your contacts to contacts.xlsx
# Columns: Name | Email

# 4. Run the script
python main.py

---

## 📁 Input / Output

**Input:** `contacts.xlsx` — Excel file with Name and Email columns

**Output:** Personalized emails land in each recipient's inbox,
console logs confirm every success and failure

---

## 🔒 Security
Credentials are stored in a `.env` file that is gitignored —
your password never touches GitHub.

---

## 💼 Use Case
Perfect for small businesses, freelancers, and agencies that need
to send personalized outreach, newsletters, follow-ups, or
onboarding emails to a list of contacts — without paying for
expensive email marketing tools like Mailchimp.
