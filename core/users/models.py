from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.dispatch import receiver


class Users(AbstractUser):
    is_freecancer=models.BooleanField(default=False)
    is_client=models.BooleanField(default=False)
    
    def __str__(self):
        return self.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)  
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
    
    

    
class Freelancer(models.Model):
    user=models.OneToOneField(Users, related_name="freelancer", on_delete=models.CASCADE)
    phone=models.CharField(max_length=15)
    skills=models.CharField(max_length=50)
    description=models.TextField
    portfolio=models.CharField
    
    def __str__(self):
        return self.username
    
class Client(models.Model):
    user=models.OneToOneField(Users, related_name="employer", on_delete=models.CASCADE )
    company_name=models.CharField(max_length=50)
    description=models.TextField
    
    def __str__(self):
        return self.company_name
    
  
