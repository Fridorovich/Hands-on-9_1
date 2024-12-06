import multiprocessing
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = int(os.getenv('SMTP_PORT'))
SMTP_USER = os.getenv('SMTP_USER')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL')

def send_email(user, message):
    msg = MIMEText(f"From user: {user}\nMessage: {message}")
    msg['Subject'] = 'New Message'
    msg['From'] = SMTP_USER
    msg['To'] = RECIPIENT_EMAIL

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.sendmail(SMTP_USER, RECIPIENT_EMAIL, msg.as_string())

def publish_service(pipe3, pipe4):
    while True:
        message = pipe3.pull()
        if message is None:
            break
        user, message = message.split(':', 1)
        send_email(user, message)
        pipe4.push(f"{user}:{message}")

if __name__ == '__main__':
    multiprocessing.freeze_support()