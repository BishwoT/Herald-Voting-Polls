from django.http import JsonResponse  
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import OTP
import random
from django.utils import timezone
from datetime import timedelta

# Generate OTP
def generate_otp():
    return ''.join([str(random.randint(0, 9)) for _ in range(6)])

# Signup view with OTP
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            return JsonResponse({"message": "Username already exists."}, status=400)

        user = User.objects.create_user(username=username, email=email, password=password)

        # Generate OTP and save it
        otp_code = generate_otp()
        otp = OTP.objects.create(
            user=user,
            otp_code=otp_code,
            expiration_time=timezone.now() + timedelta(minutes=5)
        )

        # Send OTP to email
        send_mail(
            'Your OTP for Email Validation for voting app',
            f'Your OTP is {otp_code}. It expires in 5 minutes.',
            'from@example.com',  
            [email]
        )
        return JsonResponse({"message": "OTP sent to email"})
    return render(request, 'signup.html')
