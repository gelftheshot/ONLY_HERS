from base.models import Cart, Wishlist, Shipments, Order, Review, OrderItem, Product, Category, ProductImage,Tag, SubCategory




def AllItems(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        all_cart_count = cart.cartproduct_set.count()
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        wishlist_count = wishlist.wishlistproduct_set.count()
    else:
        all_cart_count = "-"
        wishlist_count = "-"

    return {
        'all_categories': Category.objects.all(),
        'all_subcategories': SubCategory.objects.all(),
        'all_products': Product.objects.all(),
        'range_1_6': range(1, 6),
        'all_cart_count': all_cart_count,
        'wishlist_count': wishlist_count,
    }