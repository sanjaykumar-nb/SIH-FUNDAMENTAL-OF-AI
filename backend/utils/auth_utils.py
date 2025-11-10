import random
import smtplib
from email.mime.text import MIMEText

def send_otp(email: str) -> str:
    otp = str(random.randint(100000, 999999))
    print(f"OTP for {email}: {otp}")  # For demo, use console
    # Uncomment for real email
    # try:
    #     send_email(email, otp)
    # except Exception as e:
    #     print(f"Email send failed: {e}")
    return otp

def send_email(to_email: str, otp: str):
    # Configure your SMTP (example for Gmail)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = "nbsanjay3664@gmail.com"  # Replace with your email
    smtp_password = "viympujwthofobp"  # App password without spaces

    msg = MIMEText(f"Your OTP for Intelligent Enterprise Assistant is: {otp}")
    msg['Subject'] = "2FA OTP"
    msg['From'] = smtp_user
    msg['To'] = to_email

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.set_debuglevel(1)  # Enable debug output
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, to_email, msg.as_string())

def verify_otp(stored_otp: str, input_otp: str) -> bool:
    return stored_otp == input_otp
