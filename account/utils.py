import random
from django.core.mail import send_mail
from django.conf import settings

def generate_otp():
    return f"{random.randint(100000, 999999)}"

def send_otp_email(email, otp_code, purpose):
    subject = f"Your OTP Code for {purpose.replace('_', ' ').title()}"
    message = f"Your OTP code is: {otp_code}. It expires in 10 minutes."
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )
