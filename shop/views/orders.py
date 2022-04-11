from django.shortcuts import render,redirect
from shop.models.orders import Order
from django.views import View

class OrderView(View):

    def get(self,request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        return render(request, 'orders.html',{'orders': orders})
