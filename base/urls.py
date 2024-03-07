from django.urls import path
from . import views

app_name = 'base'
urlpatterns = [
    path('', views.home, name='home-page'),
    path('about/', views.about, name='about-page'),
    path('contact/', views.contact, name='contact-page'),
    path('shop/', views.shop, name='shop-page'),
    path('models/', views.models, name='models-page'),
    path('packages/', views.packages, name='packages-page'),
    path('blog/', views.blog, name='blog-page'),
    path('login/', views.login, name='login-page'),
    path('wishlist/', views.wishlist, name='wishlist-page'),
    path('cart/', views.cart, name='cart-page'),
    path('checkout/', views.checkout, name='checkout-page'),
    path('blog_deatils/', views.blog_deatils, name='blog_deatils-page'),
    path('product_details/', views.product_details, name='product_details-page'),
]