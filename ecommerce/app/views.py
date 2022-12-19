from django.shortcuts import render
from django.http import HttpResponse

def store(suman):
    return render(suman, 'store.html')

def cart(navneet):
    return render(navneet, 'cart.html')

def checkout(komal):
    return render(komal, 'checkout.html')

# Create your views here.
