from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def store(suman):
    things = Product.objects.all()
    context = {'things': things}
    return render(suman, 'store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False) #order number obtained
        items = order.orderitem_set.all() #obtained the ordered items for that order number
    else:
        items=[]

    context = {'items': items, 'order': order}
    return render(request, 'cart.html', context)

def checkout(komal):
    ord = Order.objects.all()
    orditem = OrderItem.objects.all()
    context = {'ord': ord , 'orditem': orditem}
    return render(komal, 'checkout.html', context)

# Create your views here.
