from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp_code = models.CharField(max_length=6)
    expiration_time = models.DateTimeField()

    def is_expired(self):
        return timezone.now() > self.expiration_time
