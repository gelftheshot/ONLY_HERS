from django.shortcuts import render
from django.http import HttpResponse
from base.models import (
    Cart, Shipments, Order, 
    Review, OrderItem, Product, 
    Category, ProductImage, Tag, 
    SubCategory, CartProduct, Packages, 
    Blog, Banner, Wishlist, WishlistProduct, 
    SuperModel
)
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from userauths.models import Profile
from userauths.forms import ProfileForm,ProfilePhotoForm
from django.http import JsonResponse
from django.views import View
from django.db.models import Sum
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from base.forms import ProductForm, ProductImageForm, PackagesForm, BlogForm


def dashboard(request):
    orders = Order.objects.all()
    context = {
        "orders" : orders
    }
    return render(request, 'dashboard/dashboard.html', context)


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect('dashboard:add_product_image-page', product_id=product.pro_id)
    else:
        form = ProductForm()
    return render(request, 'dashboard/add_product.html', {'form': form})



def add_product_image(request, product_id):
    product = get_object_or_404(Product, pro_id=product_id)
    if request.method == 'POST':
        form = ProductImageForm(request.POST, request.FILES)
        if form.is_valid():
            product_image = form.save(commit=False)
            product_image.product = product
            product_image.save()
            product.deatail_image = product_image
            product.save()
            return redirect('dashboard:dashboard-page')
    else:
        form = ProductImageForm()
    return render(request, 'dashboard/add_product_image.html', {'form': form})

def add_packages(request):
    if request.method == 'POST':
        form = PackagesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PackagesForm()
    return render(request, 'dashboard/add_packages.html', {'form': form})

def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BlogForm()
    return render(request, 'dashboard/add_blogs.html', {'form': form})