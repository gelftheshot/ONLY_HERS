from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'base'
urlpatterns = [
    path('', views.home, name='home-page'),
    path('about/', views.about, name='about-page'),
    path('contact/', views.contact, name='contact-page'),
    path('shop/', views.shop, name='shop-page'),
    path('shop/<str:category>/', views.shop, name='shop_by_category'),
    path('shop/<str:category>/<str:subcategory>/', views.shop, name='shop_by_subcategory'),
    path('shop/<str:category>/<str:subcategory>/<int:minprice>/<int:maxprice>/', views.shop, name='shop_by_price'),
    path('models/', views.models, name='models-page'),
    path('packages/', views.packages, name='packages-page'),
    path('blog/', views.blog, name='blog-page'),
    path('login/', views.login, name='login-page'),
    path('wishlist/', views.wishlist, name='wishlist-page'),
    path('cart/', views.cart, name='cart-page'),
    path('checkout/', views.checkout, name='checkout-page'),
    path('blog_deatils/', views.blog_deatils, name='blog_deatils-page'),
    path('product_details/', views.product_details, name='product_details-page'),
    path('blog_deatils/<str:blog_id>/', views.blog_deatils, name='blog_deatils-page'),
    path('product_details/<str:pro_id>/', views.product_details, name='product_details-page'),
    path('profile/', views.profile, name='profile-page'),
    path('add_to_cart/<str:pro_id>/', views.add_to_cart, name='add_to_cart-page'),
    path('package_to_cart/<str:pack_id>/', views.package_to_cart, name='package_to_cart-page'),
    path('def package_deatils/<str:pack_id>/', views.package_deatils, name='package_deatils-page'),
    path('product_order/', views.product_order, name='product_order-page'),
    path('place_order/', views.place_order, name = 'place_order-page'),
    path('update_profile/', views.update_profile, name = 'update_profile-page'),
    path('get_subcategories/', views.get_subcategories, name='get_subcategories'),
    path('search/', views.search, name='search-page'),
    path('wishlist/', views.wishlist, name='wishlist-page'),
    path('add_to_wishlist/<str:pro_id>/', views.add_to_wishlist, name='add_to_wishlist-page'),
    path('remove_from_cart/<str:pro_id>/', views.remove_from_cart, name = 'remove_from_cart-page'),
    path('adjust_cart/<str:pro_id>/<str:opp>', views.adjust_cart, name = 'adjust_cart-page'),
    path('remove_from_wishlist/<str:pro_id>/', views.remove_from_wishlist, name = "remove_from_wishlist-page"),
    path('supermodel/', views.supermodel, name='supermodel-page'),
    path('<str:user_name>/', views.model_by_name, name='model_by_name-page'),
    path("add_to_cart_with_qt", views.add_to_cart_with_qt, name='add_to_cart_with_qt-page'),
    # path('load_more_data/', views.load_more_data, name='load_more_data-page'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)