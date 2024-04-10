from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.safestring import mark_safe
import os
from django.conf import settings
from userauths.models import User, Profile
from django.db.models.signals import post_save
from django.dispatch import receiver

SHIPPING_STATUS_CHOICES = [
        ('SHIPPED', 'Shipped'),
        ('NOT_SHIPPED', 'Not Shipped'),
    ]
Ratting = (
    (1, '★☆☆☆☆'),
    (2, '★★☆☆☆'),
    (3, '★★★☆☆'),
    (4, '★★★★☆'),
    (5, '★★★★★'),
)

color = (
    ('Very_light', 'Very light or pale'),
    ('Light', 'Light'),
    ('Medium', 'Medium'),
    ('Olive', 'Olive'),
    ('Tan', 'Tan'),
    ('Brown', 'Brown'),
    ('Dark', 'Dark'),
    ('Very_dark', 'Very dark or black'),
)

hair = (
    ('Straight', 'Straight hair'),
    ('Wavy', 'Wavy hair'),
    ('Curly', 'Curly hair'),
    ('Kinky', 'Kinky hair'),
    ('Coarse', 'Coarse hair'),
    ('Fine', 'Fine hair'),
    ('Thick', 'Thick hair'),
    ('Thin', 'Thin hair'),
    ('Frizzy', 'Frizzy hair'),
)

skin = (
    ('Dry', 'Dry skin'),
    ('Oily', 'Oily skin'),
    ('Normal', 'Normal skin'),
    ('Combination', 'Combination skin'),
)


def get_product_upload_path(instance, filename):
    return os.path.join('category', str(instance.Category), f"{instance.name}__{instance.pro_id}" + filename)
def get_product_details_upload_path(instance, filename):
    return os.path.join('category',  "details", filename)
def get_percentage_discount(instance):
    return (instance.old_price - instance.new_price)/instance.old_price*100
def get_package_upload_path(instance, filename):
    return os.path.join('packages', f"{instance.name}", str(instance.pack_id) + filename)
def get_blog_upload_path(instance, filename):
    return os.path.join('blog', f"{instance.title}", str(instance.blog_id) + filename)
def get_subcategory_upload_path(instance, filename):
    return os.path.join('sub_category', f"{instance.name}", filename)

class Category(models.Model):
    cat_id = ShortUUIDField(unique=True, length=15, max_length=20, alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', primary_key=True, editable=False, prefix='cat')
    name = models.CharField(max_length=50)
    sub_category = models.ManyToManyField('SubCategory', blank=True, related_name='categories')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.
        directory = os.path.join(settings.MEDIA_ROOT, 'Category', self.name)
        os.makedirs(directory, exist_ok=True)
    
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Catagories'

class Product(models.Model):

    pro_id = ShortUUIDField(unique=True, length=15, max_length=20, alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', primary_key=True, editable=False, prefix='pro')
    name = models.CharField(max_length=30)
    Category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
    sub_Category = models.ForeignKey('SubCategory', on_delete=models.SET_NULL, blank=True, null=True,)
    display_image = models.ImageField(upload_to=get_product_upload_path)
    deatail_image = models.OneToOneField('ProductImage', on_delete=models.SET_NULL, blank=True, null=True, related_name='detail_product')
    new_price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, null = True, blank = True)
    description = models.TextField()
    percentage_discount = models.DecimalField(max_digits=5, decimal_places=2, null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag = models.ManyToManyField('Tag', blank=True)
    label = models.CharField(max_length=30, null = True, blank = True)
    in_stock = models.BooleanField(default=False)
    Tranding = models.BooleanField(default=False)
    Hot = models.BooleanField(default=False)
    rating = models.ForeignKey('Review', on_delete=models.SET_NULL, blank=True, null=True, related_name='rated_products')
    infulancer = models.ForeignKey('userauths.User', on_delete=models.SET_NULL, blank=True, null=True)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE, null=True)
    image1 = models.ImageField(upload_to=get_product_details_upload_path, null=True)
    image2 = models.ImageField(upload_to=get_product_details_upload_path, null=True)
    image3 = models.ImageField(upload_to=get_product_details_upload_path, null=True)
    image4 = models.ImageField(upload_to=get_product_details_upload_path, null=True)
    image5 = models.ImageField(upload_to=get_product_details_upload_path, null=True)
    image6 = models.ImageField(upload_to=get_product_details_upload_path, null=True)

    @property
    def images(self):
        return [self.image1, self.image2, self.image3, self.image4, self.image5, self.image6]

class Tag(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

class SubCategory(models.Model):
    image = models.ImageField(upload_to=get_subcategory_upload_path, null=True)
    name = models.CharField(max_length=30)
    Hot = models.BooleanField(default=False)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Sub Category'
        verbose_name_plural = 'Sub Catagories'

class Cart(models.Model):
    user = models.ForeignKey('userauths.User', on_delete=models.CASCADE)

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,)
    quantity = models.PositiveIntegerField(default=1)

class Wishlist(models.Model):
    user = models.ForeignKey('userauths.User', on_delete=models.CASCADE)

class WishlistProduct(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Shipments(models.Model):
    user = models.ForeignKey('userauths.User', on_delete=models.CASCADE)
    phone = models.CharField(max_length=30)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, null=True)
    city = models.CharField(max_length=30)
    street = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    user = models.ForeignKey('userauths.User', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=Ratting, default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment = models.TextField()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=30, null=True)
    address = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    shipped = models.CharField(
        max_length=12,
        choices=SHIPPING_STATUS_CHOICES,
        default='NOT_SHIPPED',
    )

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)


class Packages(models.Model):
    pack_id = ShortUUIDField(unique=True, length=15, max_length=20, alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', primary_key=True, editable=False, prefix='pack')
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to=get_package_upload_path, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    products = models.ManyToManyField(Product, related_name='packages', null=True)
    rating = models.ForeignKey('Review', on_delete=models.SET_NULL, blank=True, null=True, related_name='rated_package')
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True)

class Blog(models.Model):
    blog_id = ShortUUIDField(unique=True, length=15, max_length=20, alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', primary_key=True, editable=False, prefix='blog')
    title = models.CharField(max_length=100)
    author = models.ForeignKey('userauths.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_blog_upload_path, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Banner(models.Model):
    banner_id = ShortUUIDField(unique=True, length=15, max_length=20, alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', primary_key=True, editable=False, prefix='banner')
    titile = models.CharField(max_length=30, null = True)
    package = models.ForeignKey(Packages, on_delete=models.CASCADE)
    image = models.ImageField(null=True)

class Payment(models.Model):
    pass

class SuperModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=12, primary_key = True)
    instagram = models.CharField(max_length=100)
    tiktok = models.CharField(max_length=100)
    youtube = models.CharField(max_length=100, null = True)

    def __str__(self):
        return self.user.username