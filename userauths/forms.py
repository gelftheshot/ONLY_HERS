from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User
from userauths.models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['email', 'username']

class UserLoginForm(forms.Form):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name','last_name', 'city', 'phone',]

class ProfilePhotoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo']