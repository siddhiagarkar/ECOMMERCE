from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import CreateUserForm, UpdateUserForm

def store(request):
    things = Product.objects.all()
    carousels = Carousel.objects.all()
    num = len(carousels)-1
    colorzz = list(Product.objects.all().values('color').distinct())
    colorz = [u['color'] for u in colorzz]

    brands = list(Product.objects.all().values('brand').distinct())
    brandz = [u['brand'] for u in brands]
    # print(brandz)

    for i in brandz:
        # print(i)
        brandz = [i['brand'] for i in brands]
        b = Brand.objects.get(id = i)
        # b is gawd
        print(b)

    e = request.POST.get('em')
    m = request.POST.get('msg')

    context = {'things': things, 'colorz': colorz, 'colorzz': colorzz, 'carousels': carousels, 'num': num, 'brands': brands, 'b':b}
    return render(request, 'store.html', context)

def sale_view(request):
    things = Product.objects.all()
    # carousels = Carousel.objects.all()
    # num = len(carousels)-1
    # carousels only on home page

    colorzz = list(Product.objects.all().values('color').distinct())
    colorz = [u['color'] for u in colorzz]

    if request.method == 'POST':
        c = request.POST.get('car')
        print(c)
        things = Product.objects.all().filter(sale = c)

    context = {'things': things,'colorz':colorz, 'colorzz': colorzz }
    return render(request, 'store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        orderr, created = Order.objects.get_or_create(customer=customer, complete=False) #order number obtained
        items = orderr.orderitem_set.all() #obtained the ordered items for that order number
    else:
        items=[]
        orderr = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items': items, 'orderr': orderr}
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

# @csrf_exempt
def updateItem(request):
    # if request.method=="POST":

        data = json.loads(request.body)
        # prod_id = data['ProductID']
        action = data['action'] 
        prod_id = data['productId']
              
        print('Action : ', action)
        print('Product id : ', prod_id)

        customer = request.user.customer
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

# def brandview(request):
#     things = Product.objects.all()
#     if request.method == 'POST':
#         brand=request.POST.getlist('brand')
#         print(brand)

#         for x in range(len(brand)):
#             print("my chosen brand",(x+1) , brand[x])

#         if brand is not None:
#             print('you selected a brand filter!')
#             for x in range(len(brand)):
#                 things = Product.objects.filter(brand = brand[x])

#     brands = list(Product.objects.all().values('brand').distinct())
#     brand = [u['brand'] for u in brands]

#     context = {'things': things, 'brandz': brands}
#     return render(request,'store.html',context)

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

    n = request.POST.get('username')
    e = request.POST.get('email')

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            
            form.save() #GOLDEN LINE : Create Customer object after saving the form
            u=User.objects.get(username=n) #GOLDEN LINE
            Customer.objects.create(user = u, f_name = u.first_name, l_name= u.last_name, email = u.email) #GOLDEN LINE

            #log the user in
            return redirect('login')
        else:
            messages.error(request, 'Error')
            print('error')
    else:
        form = CreateUserForm()
    return render(request, 'registration.html', {'form': form})

def profile(request):
    old_user = request.user
    # submitbutton= request.POST.get('SAVE')
    # print(submitbutton)
    if request.method == 'POST':

        submitbutton= request.POST.get('submit')
        print(submitbutton)
        
        print('post')
        form = UpdateUserForm(instance=old_user, data=request.POST.get(request.user))
        if form.is_valid():
            form.save()
            Customer.objects.filter(user=old_user).update(f_name=old_user.first_name, l_name=old_user.last_name, email=old_user.email)
            return redirect('profile')

    context={'old_user':old_user, 'form':UpdateUserForm(instance=old_user)}
    return render(request, 'profile.html', context)


def wishlistview(request):
    if request.user.is_authenticated:
        wishlist = Wishlist.objects.filter(customer=request.user)
        context = {'wishlist': wishlist}
    return render(request, 'wishlist.html', context)

def productview(request, myid):
    product = Product.objects.get(id = myid)
    sizes = list(Size.objects.filter(product = product).values('size'))
    sizes = [u['size'] for u in sizes]
    print(sizes)
    context = {'product': product, 'sizes': sizes}
    return render(request, 'product.html', context)