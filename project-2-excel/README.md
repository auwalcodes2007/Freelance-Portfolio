# 🧹 Excel Data Cleaner — CSV to Formatted Excel

## 💼 The Problem
Small businesses collect data every day — customer lists, employee
records, sales logs. But that data is almost always messy:
duplicate entries, inconsistent formatting, missing fields, invalid
emails, broken phone numbers.

Cleaning this manually in Excel wastes hours and introduces human error.
This script automates the entire process in seconds.

---

## ✅ What it solves
| Problem | Fix Applied |
|---|---|
| Duplicate rows | Removed automatically |
| Inconsistent casing (JANE, jane, Jane) | Standardized to Title Case |
| Bad phone formats (spaces, dashes) | Stripped to digits only |
| Invalid emails | Flagged with ❌ in output |
| Impossible values (Age: 301) | Replaced with Unknown |
| Missing critical fields | Rows dropped cleanly |
| Unstyled raw output | Exported as formatted Excel |

---

## 🛠 Tech Stack
- Python 3.x
- Pandas
- OpenPyXL

---

## ▶️ How to run

# Install dependencies
pip install -r requirements.txt

# Run the cleaner
python main.py

---

## 📁 Input / Output

**Input:** `messy_data.csv` — raw, unstructured business data

**Output:** `cleaned_data.xlsx` — formatted Excel file with:
- Blue bold headers
- Auto-fitted column widths
- Email validation column
- All formatting standardized

---

## 💼 Use Case
Any business sitting on messy spreadsheets — clinics, logistics
companies, schools, retail stores — can hand you their raw CSV
and get back a clean, professional Excel file ready for reporting
or importing into their systems.
