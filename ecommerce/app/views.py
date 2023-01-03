from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json

def store(request):
    things = Product.objects.all()
    mylist=request.POST.getlist('gendercheck')

    if request.GET.get('Apply') == 'Apply':
        print('user clicked apply')
        if 'Female' in mylist:
            things = Product.objects.filter(tag = True)
        elif 'Male' in mylist:
            things = Product.objects.filter(tag = False)

    context = {'things': things}
    return render(request, 'store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False) #order number obtained
        items = order.orderitem_set.all() #obtained the ordered items for that order number
    else:
        items=[]
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items': items, 'order': order}
    return render(request, 'cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False) #order number obtained
        items = order.orderitem_set.all() #obtained the ordered items for that order number
    else:
        items=[]
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items': items, 'order': order}
    return render(request, 'checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    prod_id = data['prod_id']
    action = data['action']
    print('Action : ', action)
    print('Product : ', prod_id)

    return JsonResponse('Item was added', safe=False)
