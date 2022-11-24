from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from shop.models import Product
from .models import *
# Create your views here.
from .import forms

def cart_init(request):
    try:
        cart = Cart.objects.get(id=request.session.get('user_cart_id'))
    except:
        cart = Cart.objects.create()
        request.session['user_cart_id'] = cart.id
    return cart


def cart_view(request):
    item_counter = 0
    try:
        cart = Cart.objects.get(id=request.session.get('user_cart_id'))
    except:
        cart = {'notfound': "Products not found!"}
    return render(request,'cart/cart_view.html', {'cart':cart})

import json
def addToCart(request):
    d = request.GET.get('data')
    data = json.loads(d)
    cart = cart_init(request)
    cart.add(data['product_id'],data['count'])
    if cart:
        status = {
            'status':200
        }
    else:
        status = {
            'status': 200
        }
    return JsonResponse(status)

def delete_item(request, product_id, qty):
    cart = Cart.objects.get(id=request.session.get('user_cart_id'))
    cart.deleteItem(product_id, qty)

    return redirect('shop:home')

def remove(request):
    print(request.path)
    try:
        cart = Cart.objects.get(id=request.session.get('user_cart_id'))
    except:
        return redirect('shop:home')
    cart.delete()
    return redirect('shop:home')

# Orders view
def addOrder(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    if request.method == 'POST':
        form = forms.AddOrderForm(request.POST)
        if form.is_valid():
            f = form.save()
            for p in cart.products.all():
                f.products.create(
                    product=p.product,
                    quantity=p.quantity,
                    price=p.quantity * p.price
                )
            f.payed = False
            f.total_sum = cart.total_price
            f.save()
            order = Order.objects.last()
            return render(request,'cart/order_done.html', {'order':order})
    else:
        form = forms.AddOrderForm()
    return render(request, 'cart/order.html', {'form':form})

def orderDone(request):
    return render(request, 'cart/order_done.html')