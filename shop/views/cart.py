
from django.shortcuts import redirect,render
from django.views import View
from shop.models.product import Product

class Cart(View):
    def get(self,request):
        if request.session.get('cart').keys():
            cart = list(request.session.get('cart').keys())
            product = Product.get_product_by_id(cart)
            print(product)
            return render(request,'cart.html',{'cart_product' : product}) 
        else:
            product = {}
            return render(request,'cart.html',{'cart_product':product})

            

