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
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import JsonResponse
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



def home(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        all_cart_count = cart.cartproduct_set.count()
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        wishlist_count = wishlist.wishlistproduct_set.count()
    else:
        all_cart_count = 0
        wishlist_count = 0

    product = Product.objects.all()
    total = Product.objects.all().count()
    category = Category.objects.all()
    subcategory = SubCategory.objects.all()
    banner = Banner.objects.all()
    context = {
        'product': product,
        'category': category,
        'range_1_6': range(1, 6),
        'len': 5,
        'all_cart_count': all_cart_count,
        'subcategory': subcategory,
        'total': total,
        'banner': banner,
        'wishlist_count': wishlist_count,
    }
    return render(request, 'base/index.html', context)



# def load_more_data(request):
#     try:
#         offset = int(request.GET.get('offset', 0))
#         limit = int(request.GET.get('limit', 5))
#         product = Product.objects.all()[offset:offset+limit]
#         total = Product.objects.all().count()
#         html = render_to_string('base/index', {'product': product})
#         return JsonResponse({'html': html, 'total': total})
#     except Exception as e:
#         return JsonResponse({'error': str(e)})


def pages():
    return render(request, 'base/pages.html')
def about(request):
    return render(request, 'base/about.html')

def contact(request):
    return render(request, 'base/contact.html')

def shop(request, category=None, subcategory=None,):
    if category and subcategory:
        products = Product.objects.filter(Category__name=category, sub_Category__name=subcategory)
    elif category:
        products = Product.objects.filter(Category__name=category)
        subcategory = SubCategory.objects.filter(Category__name=category)
    else:
        products = Product.objects.all()
        category = Category.objects.all()
        subcategory = SubCategory.objects.all()

    context = {
        'products': products,
        'category': category,
        'subcategory': subcategory,
        'range_1_6': range(1, 6),
    }
    return render(request, 'base/shop.html', context)
def models(request):
    return render(request, 'base/models.html')

def packages(request):

    packages = Packages.objects.all()
    context = {
        'packages': packages,
    }
    return render(request, 'base/packages.html', context)

def blog(request):

    blog = Blog.objects.all()

    context = {
        'blogs': blog,
    }
    return render(request, 'base/blog.html', context)

def login(request):
    return render(request, 'base/login.html')

def cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('pro_id')
        quantity = request.POST.get('quantity')

        try:
            # Get the cart and the product
            cart = Cart.objects.get(user=request.user)  # Replace with your actual cart
            product = Product.objects.get(id=product_id)

            # Get the CartProduct instance for this cart and product
            cart_product = CartProduct.objects.get(cart=cart, product=product)

            # Update the quantity
            cart_product.quantity = int(quantity)
            cart_product.save()

            # Recalculate the total
            new_total = cart_product.quantity * product.price

            return JsonResponse({'new_total': new_total})
        except (Cart.DoesNotExist, Product.DoesNotExist, CartProduct.DoesNotExist):
            raise Http404("Cart, product or cart product not found")
    else:
        try:
            if request.user.is_authenticated:
                cart = Cart.objects.get(user=request.user)
                cart_products = CartProduct.objects.filter(cart=cart)
                total = sum(pro.product.new_price * pro.quantity for pro in cart_products)
                context = {
                    'cart_products': cart_products,
                    'range_1_6': range(1, 6),
                    'total': total
                }
                return render(request, 'base/cart.html', context)
            else:
                return redirect('userauths:login-page')
        except Cart.DoesNotExist:
            raise Http404("Cart not found")


@login_required(login_url='userauths:login-page')
def wishlist(request):
    
    wishlist = Wishlist.objects.get(user=request.user)
    wishlist_products = WishlistProduct.objects.filter(wishlist=wishlist)
    
    if not wishlist_products.exists():
        messages.info(request, "Nothing in your wishlist")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    context = {
        'products': wishlist_products,
        'range_1_6': range(1, 6),
    }
    return render(request, 'base/wishlist.html', context)

def blog_deatils(request, blog_id):

    blog = Blog.objects.get(blog_id=blog_id)
    context = {
        'blog': blog
    }
    return render(request, 'base/blog-details.html', context)

def package_deatils(request, pack_id):

    package = Packages.objects.get(pack_id=pack_id)
    context = {
        'package': package
    }
    return render(request, 'base/package-details.html', context)


def checkout(request):
    return render(request, 'base/checkout.html')

def product_details(request, pro_id):

    product = Product.objects.get(pro_id=pro_id)
    context = {
        'product': product
    }
    return render(request, 'base/product-details.html', context)

@login_required(login_url='userauths:login-page')
def profile(request):
    user = request.user
    orders = Order.objects.filter(user=user)
    for order in orders:
        order.total = order.orderitem_set.aggregate(total=Sum('total_price'))['total']
    profile, created = Profile.objects.get_or_create(user=request.user)
    profile_form = ProfileForm(instance=profile)
    photo_form = ProfilePhotoForm(instance=profile)
    context = {
        'user': user,
        'orders': orders,
        'profile_form': profile_form,
        'photo_form': photo_form
    }
    return render(request, 'base/user_profile.html', context)



def add_to_cart(request, pro_id):
    if not request.user.is_authenticated:
        return JsonResponse({
            'redirect': True,
            'redirect_url': reverse('userauths:login-page')
        })

    product = get_object_or_404(Product, pro_id=pro_id)

    if product.new_price == 0:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_product, created = CartProduct.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_product.quantity += 1
        cart_product.save()

    cart_count = Cart.objects.get(user=request.user).cartproduct_set.count()
    wishlist_count = Wishlist.objects.get(user=request.user).wishlistproduct_set.count()
    return JsonResponse({'cart_count': cart_count, 'wishlist_count': wishlist_count})

def add_to_wishlist(request, pro_id):
    if not request.user.is_authenticated:
        return JsonResponse({
            'redirect': True,
            'redirect_url': reverse('userauths:login-page')
        })

    product = get_object_or_404(Product, pro_id=pro_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist_product, created = WishlistProduct.objects.get_or_create(wishlist=wishlist, product=product)
    if created:
        wishlist_product.save()
    cart_count = Cart.objects.get(user=request.user).cartproduct_set.count()
    wishlist_count = Wishlist.objects.get(user=request.user).wishlistproduct_set.count()
    return JsonResponse({'cart_count': cart_count, 'wishlist_count': wishlist_count})

@login_required(login_url='userauths:login-page')
def package_to_cart(request, pack_id):
    package = get_object_or_404(Packages, pack_id=pack_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    if package.total_price == 0:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    for product in package.products.all():
        cart_product, created = CartProduct.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_product.quantity += 1
            cart_product.save()

@login_required(login_url='userauths:login-page')
def product_order(request):
    cart = Cart.objects.get(user=request.user)
    cart_products = CartProduct.objects.filter(cart=cart)

    if not cart_products.exists():
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    total = sum(pro.product.new_price * pro.quantity for pro in cart_products)
    profile, created = Profile.objects.get_or_create(user=request.user)
    profile_form = ProfileForm(instance=profile)

    context = {
        'profile_form': profile_form,
        'cart_products': cart_products,
        'range_1_6': range(1, 6),
        'total': total
    }
    return render(request, 'base/order.html', context)

@login_required(login_url='userauths:login-page')
def place_order(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    form = ProfileForm(request.POST, instance=profile)
    if form.is_valid():
        form.save()

    cart = Cart.objects.get(user=request.user)
    cart_items = CartProduct.objects.filter(cart=cart)

    if not cart_items.exists():
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    order = Order(user=request.user)
    order.save()

    for item in cart_items:
        total_price = item.product.new_price * item.quantity
        order_item = OrderItem(order=order, product=item.product, quantity=item.quantity, total_price = total_price)
        order_item.save()

    cart_items.delete()
    return redirect('base:profile-page')


def update_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
        photo_form = ProfilePhotoForm(request.POST, request.FILES, instance=profile)
        if photo_form.is_valid():
            photo_form.save()
        return redirect('base:profile-page')
    else:
        form = ProfileForm(instance=profile)
        photo_form = ProfilePhotoForm(instance=profile)

    context = {'form': form, 'photo_form': photo_form}
    return render(request, 'base/user_profile.html', context)


def get_subcategories(request):
    category_id = request.GET.get('category_id')
    category = Category.objects.get(cat_id=category_id)
    subcategories = category.sub_category.all()
    subcategory_list = list(subcategories.values('id', 'name'))
    return JsonResponse(subcategory_list, safe=False)

def search(request):
    query = request.GET.get('q')
    product = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'base/search_results.html', {'products': product})

def remove_from_cart(request, pro_id):
    print('removed from cart')
    product = get_object_or_404(Product, pro_id=pro_id)
    cart = Cart.objects.get(user=request.user)
    cart_product = CartProduct.objects.get(cart=cart, product=product)
    cart_product.delete()
    cart_count = Cart.objects.get(user=request.user).cartproduct_set.count()
    return JsonResponse({'cart_count': cart_count})

def remove_from_wishlist(request, pro_id):
    product = get_object_or_404(Product, pro_id=pro_id)
    wishlist = Wishlist.objects.get(user=request.user)
    wishlist_product = WishlistProduct.objects.get(wishlist=wishlist, product=product)
    wishlist_product.delete()
    wishlist_count = Wishlist.objects.get(user=request.user).wishlistproduct_set.count()
    return JsonResponse({'wishlist_count': wishlist_count,})


@login_required(login_url='userauths:login-page')
def adjust_cart(request, pro_id, opp):

    product = get_object_or_404(Product, pro_id=pro_id)

    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_product, created = CartProduct.objects.get_or_create(cart=cart, product=product)
    if not created:
        if opp == 'add':
            cart_product.quantity += 1
            cart_product.save()
        elif opp == 'subtract':
            if cart_product.quantity > 1:
                cart_product.quantity -= 1
                cart_product.save()
            else:
                cart_product.delete()
                deleted = True
    return JsonResponse({'quantity': cart_product.quantity})


def supermodel(request):
    models = SuperModel.objects.all()

    context = {
        'models': models
    }
    return render(request, 'base/supermodels.html', context)

def supermodel_details(request, id):
    model = SuperModel.objects.get(id=id)
    context = {
        'model': model
    }
    return render(request, 'base/models_detail.html', context)