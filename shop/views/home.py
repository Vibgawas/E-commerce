from itertools import product
from shop.models.category import Category
from shop.models.product import Product
from django.shortcuts import render,redirect
from django.views import View


# Create your views here.
class Index(View):

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}

        prds = None
        catg = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            prds = Product.get_all_products_by_id(categoryID)
        else:
            prds = Product.get_all_products()
        

        data = {'categories':catg,'products':prds}
        return render(request, 'index.html',data)

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                   if quantity <=1:
                       cart.pop(product)
                   else:
                       cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        return redirect('home')

