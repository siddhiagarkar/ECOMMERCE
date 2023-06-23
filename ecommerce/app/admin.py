from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Product)
admin.site.register(Shipping)
admin.site.register(Carousel)
admin.site.register(Message)
admin.site.register(Size)
admin.site.register(Brand)