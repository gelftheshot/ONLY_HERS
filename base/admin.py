from django.contrib import admin
from base.models import (
    Cart, Shipments, Order, 
    Review, OrderItem, Product, 
    Category, ProductImage, Tag, 
    SubCategory, CartProduct, Packages, 
    Blog, Banner, Wishlist, WishlistProduct, 
    SuperModel)
from django.utils.html import format_html

# Register your models here.

class ProductImageAdmin(admin.StackedInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'new_price', 'old_price', 'display_image']

    def display_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.display_image.url)
    display_image.short_description = 'Image'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'sub_Category':
            selected_category_id = request.POST.get('Category')
            kwargs['queryset'] = SubCategory.objects.filter(Category_id=selected_category_id)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    class Meta:
        model = Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    class Meta:
        model = Category

class CartProductAdmin(admin.ModelAdmin):

    list_display = ["display_product", 'quantity',]

    def display_product(self, obj):
        return obj.product.name
    display_product.short_description = 'Product'

    class Meta:
        model = Cart

class CartAdmin(admin.ModelAdmin):
    model = Cart
class WishlistAdmin(admin.ModelAdmin):
    class Meta:
        model = Wishlist

class WishlistProductAdmin(admin.ModelAdmin):
    list_display = ["display_product"]
    def display_product(self, obj):
        return obj.product.name
    display_product.short_description = 'Product'
    class Meta:
        model = WishlistProduct
class ShipmentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'city', 'phone', 'email',]
    class Meta:
        model = Shipments

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'city',]
    class Meta:
        model = Order
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['display_product', 'quantity', 'total_price',]

    def display_product(self, obj):
        return obj.product.name
    display_product.short_description = 'Product'

    class Meta:
        model = OrderItem
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['display_product', 'user', 'rating', 'comment']

    class Meta:
        model = Review

    def display_product(self, obj):
        return obj.product.name
    display_product.short_description = 'Product'

class PackagesAdmin(admin.ModelAdmin):
    list_display = ['name', 'total_price', 'description']

    class Meta:
        model = Packages

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', ]
    class Meta:
        model = Blog
class BannerAdmin(admin.ModelAdmin):
    list_display = ['image', 'titile']
    class Meta:
        model = Banner
class SuperModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'profile', 'instagram', 'tiktok']
    class Meta:
        model = SuperModel

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory)
admin.site.register(Tag,)
admin.site.register(Cart, CartAdmin)
admin.site.register(Shipments, ShipmentsAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(CartProduct, CartProductAdmin)
admin.site.register(Packages, PackagesAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(WishlistProduct, WishlistProductAdmin)
admin.site.register(SuperModel, SuperModelAdmin)
