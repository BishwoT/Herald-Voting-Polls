# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
import random
from .models import OTP
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from myproject.models import OTP  # OTP model should be defined
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import OTP
import random
from django.utils import timezone
from datetime import timedelta


from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import OTP
from random import randint

# Signup view
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from .models import OTP
from random import randint
from django.db import IntegrityError

# Signup view
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        # Get the user model
        User = get_user_model()
        
        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            # Email already exists
            return render(request, 'signup.html', {'error': 'Email is already taken'})
        
        try:
            # Create the user
            user = User.objects.create_user(username=username, email=email, password=password)
            
            # Generate OTP
            otp_code = randint(100000, 999999)
            
            # Create OTP entry in the database
            otp_instance = OTP.objects.create(user=user, otp_code=otp_code)
            
            # Send OTP via email
            send_mail(
                'Your OTP code',
                f'Your OTP code is {otp_code}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            
            # Redirect to OTP verification page
            return redirect('verify_otp', user_id=user.id)
        
        except IntegrityError:
            # Handle email already in use
            return render(request, 'signup.html', {'error': 'Email already exists'})
    
    return render(request, 'signup.html')


def generate_otp():
    return ''.join([str(random.randint(0, 9)) for _ in range(6)])


#OTP verification
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from myproject.models import OTP

def verify_otp(request, user_id):
    if request.method == 'POST':
        otp_code = request.POST['otp_code']
        
        try:
            otp_instance = OTP.objects.get(user_id=user_id, otp_code=otp_code)
            
            if otp_instance.is_expired():
                return render(request, 'verify_otp.html', {'error': 'OTP has expired', 'user_id': user_id})
            
            otp_instance.is_used = True
            otp_instance.save()

            # Proceed with the user login process here

            return redirect('home')  # Redirect to home page after successful OTP verification

        except OTP.DoesNotExist:
            return render(request, 'verify_otp.html', {'error': 'Invalid OTP', 'user_id': user_id})

    return render(request, 'verify_otp.html', {'user_id': user_id})





from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after login
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')




# home view after login
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login if the user is not authenticated
    
    return render(request, 'home.html')



#logout
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout
