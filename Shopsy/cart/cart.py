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

