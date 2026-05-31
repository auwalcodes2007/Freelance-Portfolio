from dotenv import load_dotenv
import os
import openpyxl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib


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
def build_email(contact):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = contact['email']
    msg['Subject'] = f"Hey {contact['name'].split()[0]}, a quick message for you"

    body = f"""
Hi {contact['name'].split()[0]},

Hope you're doing well! I'm reaching out to introduce my Python
automation services. I help businesses save time by automating
repetitive tasks like data cleaning, report generation, and
email outreach — exactly like this email was sent.

If that sounds useful, I'd love to chat.

Best regards,
Mohammed Auwal Hassan
    """
    msg.attach(MIMEText(body, "plain"))
    return msg


# --- SEND EMAILS ---


# --- MAIN ---
