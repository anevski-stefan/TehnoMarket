from django.contrib import admin

from TehnoMarket.models import Category, Product, CustomUser, Comment, PaymentMethod, Role, Cart, CartItem, Order

# Register your models here.
admin.site.register(Category)
admin.site.register(CustomUser)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(PaymentMethod)
admin.site.register(Role)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
