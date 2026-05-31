from dotenv import load_dotenv
import os
import openpyxl


# LOAD CREDENTIALS
load_dotenv()
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# --- READ CONTACTS FROM EXCEL ---
def load_contacts(file_path):
    wb = openpyxl.load_workbook(file_path)
    ws = wb.active()
    contacts = []
    for row in ws.iter_rows(min=2, values_only=True):
        name, email = row
        if name and email:
            contacts.append({"name": name, "email": email})
    return contacts


# --- BUILD PERSONALIZED EMAIL ---


# --- SEND EMAILS ---


# --- MAIN ---
