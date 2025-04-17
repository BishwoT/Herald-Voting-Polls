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


#forgot password 

import random
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import OTP
from .forms import OTPForm
from django.utils.crypto import get_random_string

def generate_otp(user):
    otp_code = get_random_string(length=6, allowed_chars='0123456789')
    OTP.objects.create(user=user, otp_code=otp_code)
    send_mail(
        'Your OTP code for password reset',
        f'Your OTP code is: {otp_code}',
        'np03cs4s240019@heraldcollege.edu.np', 
        [user.email],
        fail_silently=False,
    )
    return otp_code

def forgot_password(request):
    if request.method == "POST":
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
            otp_code = generate_otp(user)
            return redirect('verify_otp', user_id=user.id)
        except User.DoesNotExist:
            return render(request, 'forgot_password.html', {'error': 'Email not found.'})
    return render(request, 'forgot_password.html')

# myapp/views.py

from django.shortcuts import render, redirect
from django.urls import reverse
from .models import OTP

def verify_otp(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == "POST":
        form = OTPForm(request.POST)
        if form.is_valid():
            otp_code = form.cleaned_data['otp_code']
            otp = OTP.objects.filter(user=user, otp_code=otp_code, is_used=False).first()
            if otp and not otp.is_expired():
                otp.is_used = True
                otp.save()
                # Redirect to the 'reset_password' page (ensure the URL pattern exists)
                return redirect('reset_password', user_id=user.id)
            else:
                return render(request, 'verify_otp.html', {'error': 'Invalid or expired OTP.'})
    else:
        form = OTPForm()
    return render(request, 'verify_otp.html', {'form': form})

# myapp/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  
