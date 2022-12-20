from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def store(suman):
    things = Product.objects.all()
    context = {'things': things}
    return render(suman, 'store.html', context)

def cart(navneet):
    ord = Order.objects.all()
    orditem = OrderItem.objects.all()
    context = {'ord': ord , 'orditem': orditem}
    return render(navneet, 'cart.html', context)

def checkout(komal):
    ord = Order.objects.all()
    orditem = OrderItem.objects.all()
    context = {'ord': ord , 'orditem': orditem}
    return render(komal, 'checkout.html', context)

# Create your views here.
