from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Brand(models.Model):
    name = models.CharField(null=True, max_length= 200)

    def __str__(self):
        return self.name

class Carousel(models.Model):
    image = models.ImageField(blank=True, null=True)
    slide_number = models.IntegerField(null=True)
    title = models.CharField(null=True, max_length= 200)
    description = models.CharField(null=True, max_length= 200)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    f_name = models.CharField(null=True, max_length=40)
    l_name = models.CharField(null=True, max_length=40)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.f_name

class Product(models.Model):
    item = models.CharField(null=True, max_length= 200)
    image = models.ImageField(blank=True, null=True)
    price = models.IntegerField(null = True)
    sale = models.ForeignKey(Carousel, null=True, blank=True, on_delete=models.CASCADE, related_name="sale")
    brand = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.CASCADE, related_name="brand")
    saleprice = models.IntegerField(null = True, blank=True)
    TAG_CHOICES = ((True, 'Women'), (False, 'Men'))
    tag = models.BooleanField(choices = TAG_CHOICES, null=None, default=True)
    instocknumber = models.IntegerField(null=True)
    availability = models.BooleanField(null=True)
    color = models.CharField(null=True, max_length= 20)

    def clean(self):
        if self.instocknumber == 0:
            self.availability = False
        else:
            self.availability = True

    def __str__(self):
        return self.item

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Order(models.Model):
    customer = models.ForeignKey(Customer, null= True, blank = True, on_delete=models.SET_NULL)
    orderdate = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=40, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_quantity for item in orderitems])
        return total
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    orderitemdate = models.DateTimeField(auto_now_add=True)
# no def

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    @property
    def get_quantity(self):
        total = sum([self.quantity for item in self.product.order])
        return total
class Wishlist(models.Model):
    customer = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.product.item

class Shipping(models.Model):
    customer = models.ForeignKey(Customer, null=True,on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=300, null=False)
    state = models.CharField(max_length=50, null=False)
    city = models.CharField(max_length= 50, null=False)
    pincode = models.IntegerField(null=True, blank = True)

    def __str__(self):
        return self.address
    
# class Message(models.Model):
#     email = models.EmailField(null=True)
#     subject = models.CharField(null=True, max_length= 200)

#     def __str__(self):
#         return self.email
    
SIZE_CHOICES = (
    ("XXS", "XXS"),
    ("XS", "XS"),
    ("S", "S"),
    ("M", "M"),
    ("L", "L"),
    ("XL", "XL"),
    ("XXL", "XXL"),
    ("XXXL", "XXXL"),
)   
class Size(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    size = models.CharField(null=True, max_length= 20, choices=SIZE_CHOICES, default='M')
    quantity = models.IntegerField(null=True, blank = True)

    def __str__(self):
        return self.product.item + " " + self.size