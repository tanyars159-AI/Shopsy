from store.models import Products

class Cart():
    def __init__(self,request):
        self.session = request.session

        #if current session exists get it
        cart = self.session.get('session_key')

        #if user is new then create one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        #to make cart available on all pages
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)


        #logic 
        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

    def cart_total(self):
        #get product ids
        product_ids = self.cart.keys()
        #look for ids in products database
        products = Products.objects.filter(id__in=product_ids)
        quantities = self.cart

        total = 0
        for key, value in quantities.items():
            #convert key string to numeric
            key = int(key)
            for product in products:
                if product.id == key:
                    total = total + (product.price * value)

        return total


    
    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        #get ids
        product_ids = self.cart.keys()

        #use ids to look products in database model
        products = Products.objects.filter(id__in = product_ids)

        #return products after looking up
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities

    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        #get cart
        mycart = self.cart
        #update cart
        mycart[product_id] = product_qty

        self.session.modified = True

        thing = self.cart
        return thing

    def delete(self,product):
        product_id = str(product)

        #deleting it from cart
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True


