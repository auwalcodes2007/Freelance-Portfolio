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
INPUT_FILE = 'contacts.xlsx'

# --- READ CONTACTS FROM EXCEL ---
def load_contacts(file_path):
    wb = openpyxl.load_workbook(file_path)
    ws = wb.active
    contacts = []
    for row in ws.iter_rows(min_row=2, values_only=True):
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
def send_emails(contacts):
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            print("✅ Logged in successfully\n")

            for contact in contacts:
                msg = build_email(contact)
                try:
                    smtp.sendmail(EMAIL_ADDRESS, contact['email'], msg.as_string())
                    print(f"📧 Sent to {contact['name']} — {contact['email']}")
                except Exception as e:
                    print(f"❌ Failed to send to {contact['email']}: {e}")

    except Exception as e:
        print(f"❌ Login failed: {e}")


# --- MAIN ---
if __name__ == '__main__':
    contacts = load_contacts(INPUT_FILE)
    print(f"📋 Loaded {len(contacts)} contacts\n")
    send_emails(contacts)
    print("\n🎉 Done!")