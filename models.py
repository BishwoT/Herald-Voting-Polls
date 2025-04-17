from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp_code = models.CharField(max_length=6)
    expiration_time = models.DateTimeField()

    def is_expired(self):
        return timezone.now() > self.expiration_time


#forgot password otp
# myapp/models.py



# myapp/models.py
from django.db import models
from django.utils import timezone
from datetime import timedelta

class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp_code = models.CharField(max_length=6)  # OTP length
    created_at = models.DateTimeField(auto_now_add=True) 
    is_used = models.BooleanField(default=False)

    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(minutes=5)  

    def __str__(self):
        return f"OTP for {self.user.username}"

