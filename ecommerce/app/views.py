from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def store(request):
    things = Product.objects.all()
    colorzz = list(Product.objects.all().values('color').distinct())
    colorz = [u['color'] for u in colorzz]
    context = {'things': things, 'colorz': colorz, 'colorzz': colorzz}
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

@csrf_exempt
def updateItem(request):
    if request.method=="POST":
        data = json.loads(request.body)
        prod_id = data['ProductID']
        action = data['Action']       
        print('Action : ', action)
        print('Product id : ', prod_id)

        customer, created = Customer.objects.get_or_create(user=request.user)
        product = Product.objects.get(id = prod_id)
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

        if action=='add':
            orderItem.quantity = (orderItem.quantity+1)
        elif action=='remove':
            orderItem.quantity = (orderItem.quantity-1)
        orderItem.save()
        if orderItem.quantity<=0:
            orderItem.delete()

        return JsonResponse('Item was added', safe=False)

def searchview(request):
    things = Product.objects.all()
    term = request.GET.get('searchname', None)
    if term:
        things=Product.objects.filter(item__icontains=term)

    colorzz = list(Product.objects.all().values('color').distinct())
    colorz = [u['color'] for u in colorzz]

    context = {'things': things, 'colorz': colorz}
    return render(request,'store.html',context)

def filterview(request):
    things = Product.objects.all()
    print('f')
    mylist=request.GET.getlist('gendercheck')
    if 'Male' in mylist:
        things=Product.objects.filter(tag=False)
    elif 'Men' and 'Women' in mylist:
        things=Product.objects.all()
    else:
        things=Product.objects.filter(tag=True)

    colorzz = list(Product.objects.all().values('color').distinct())
    colorz = [u['color'] for u in colorzz]
    context = {'things': things, 'colorz': colorz}
    return render(request,'store.html',context)

def sortview(request):
    things = Product.objects.all()
    print("in")
    if request.method == 'POST':
        sortby=request.POST.get('sort')
        print(sortby)
        if sortby == 'Price: Low to High':
            things = Product.objects.all().order_by('price')
        elif sortby == 'Price: High to Low':
            things = Product.objects.all().order_by('-price')
        # elif sortby == 'disc':
        #     things = Product.objects.all().order_by('item')
        # elif sortby == 'rating':
        #     things = Product.objects.all().order_by('-item')
        else:
            things = Product.objects.all()

    # colorzz = list(Product.objects.all().values('color').distinct())
    # colorz = [u['color'] for u in colorzz]
    context = {'things': things}
    return render(request,'store.html',context)

def colorview(request):
    things = Product.objects.all()
    if request.method == 'POST':
        colorz=request.POST.getlist('color')
        print(colorz)

        for x in range(len(colorz)):
            print("my chosen colour",(x+1) , colorz[x])

        if colorz is not None:
            print('you selected a color filter!')
            for x in range(len(colorz)):
                things = Product.objects.filter(color = colorz[x])

    colorzz = list(Product.objects.all().values('color').distinct())
    colorz = [u['color'] for u in colorzz]

    context = {'things': things, 'colorz': colorz}
    return render(request,'store.html',context)

def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect('store')
    else:
        alert = 'Invalid credentials'
        m = messages.error(request, 'Error')
        message = str(m)

    context = {}
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('store')
    # Redirect to a success page.

def registration_view(request):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'customer', null=True, blank=True)
    e = request.POST.get('email')
    n = request.POST.get('username')
    u = request.user
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            fld = Customer.objects.create(user = u, name = n, email = e)
            form.save()
            #log the user in
            return redirect('login')
        else:
            messages.error(request, 'Error')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})

