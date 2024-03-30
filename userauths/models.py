from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)
    username = models.CharField(max_length=100, unique=True, blank=False, null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    profile_photo = models.ImageField(upload_to='profile_photos/', default='default.jpg')  
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

