from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from django.conf import settings

# Custom Manager for the User Model
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)  # Hashes the password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, username, password, **extra_fields)

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50)
    role = models.CharField(max_length=20, choices=[('voter', 'Voter'), ('admin', 'Admin')], default='voter')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta

class OTP(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(default=timezone.now)
    expiration_time = models.DateTimeField(null=True, blank=True)

    def is_expired(self):
        if self.expiration_time is None:
            return False
        return timezone.now() > self.expiration_time
