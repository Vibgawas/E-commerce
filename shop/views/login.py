
from django.contrib.auth.hashers import check_password
from django.views import View
from django.shortcuts import render,HttpResponse,redirect
from shop.models.customer import Customer

from shop.models import customer
class Login(View):
    return_url = None

    def get(self,request):
        Login.return_url = request.GET.get('return_url')
        return render(request,'login.html')

    def post(self,request):
        post_data = request.POST
        email = post_data.get('email')
        password = post_data.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password,customer.password)
            if flag:
                request.session['customer'] = customer.id
                if Login.return_url:
                    return HttpResponse(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('home')
            else:
                error_message = "Password Invalid..!!"
        else:
            error_message = "Invalid email...!!"

        return render(request,'login.html',{'error':error_message})


def logout(request):
    request.session.clear()
    return redirect('login')