from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Products
from django.http import JsonResponse

# Create your views here.
def cart_summary(request):
    #get the cart
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    return render(request,"cart_summary.html",{"cart_products": cart_products, "quantities": quantities})

def cart_add(request):
    # get cart
    cart = Cart(request)
    # test for post
    if request.POST.get('action') =='post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))


        product = get_object_or_404(Products, id=product_id)
        #save to session
        cart.add(product=product, quantity=product_qty)
        #get cart quantity
        cart_quantity = cart.__len__()

        #return response
        #response = JsonResponse({'Product Name': product.name})
        response = JsonResponse({'qty': cart_quantity})
        return response

def cart_delete(request):
    return render(request,'cart_delete.html',{})

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') =='post':
        # get things
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        product = get_object_or_404(Products, id=product_id)

        cart.update(product=product_id,quantity=product_qty)

        response = JsonResponse({'qty': product_qty})
        return response