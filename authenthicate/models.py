from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phonenumber = PhoneNumberField()
    city = models.CharField(max_length=50)
    def __str__(self):
        return self.user.username


class CafeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cafeName = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    def __str__(self):
        return self.user.username