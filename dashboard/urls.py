from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard-page'),
    path('add_product/', views.add_product, name='add_product-page'),
    path('add_product_image/<str:product_id>/', views.add_product_image, name='add_product_image-page'),    
    path('add_packages/', views.add_packages, name='add_packages-page'),
    path('add_blog/', views.add_blog, name='add_blog-page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)