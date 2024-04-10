from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User
from userauths.models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from base.models import Product, ProductImage, Packages, Blog

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'Category', 'display_image', 'new_price', 'old_price', 'description', 'sub_Category',]


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image1', 'image2', 'image3', 'image4', 'image5', 'image6']

class PackagesForm(forms.ModelForm):
    class Meta:
        model = Packages
        fields = ['name', 'description', 'image', 'total_price', 'products', 'rating', 'discount']


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'author', 'image', 'content']