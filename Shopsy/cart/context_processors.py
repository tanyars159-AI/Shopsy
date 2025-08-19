from .cart import Cart

#to make cart works on all pages
def cart(request):
    #return default data from our Cart
    return {'cart': Cart(request)}