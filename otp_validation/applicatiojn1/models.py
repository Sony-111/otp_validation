from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.conf import settings
import secrets
from django.utils import timezone
from datetime import timedelta

class CustomUser(AbstractUser):
    email=models.EmailField(unique=True)
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['username',]
    def __str__(self):
        return self.email
    

class OtpToken(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='otps')
    otp_code=models.CharField(max_length=6)
    otp_created_at=models.DateTimeField(auto_now_add=True)
    otp_expires_at=models.DateTimeField(blank=True, null=True)

    def save(self,*args, **kwargs):
        if not self.otp_code:
            self.otp_code=secrets.token_hex(3)
        if not self.otp_expires_at:
            self.otp_expires_at=timezone.now()+timedelta(minutes=5)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.user.username
