from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'base/index.html')

def about(request):
    return render(request, 'base/about.html')

def contact(request):
    return render(request, 'base/contact.html')

def shop(request):
    return render(request, 'base/shop.html')

def models(request):
    return render(request, 'base/models.html')

def packages(request):
    return render(request, 'base/packages.html')

def blog(request):
    return render(request, 'base/blog.html')

def login(request):
    return render(request, 'base/login.html')

def wishlist(request):
    return render(request, 'base/wishlist.html')

def cart(request):
    return render(request, 'base/cart.html')