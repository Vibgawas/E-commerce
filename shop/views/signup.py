
from django.contrib.auth.hashers import make_password
from shop.models.customer import Customer
from django.shortcuts import redirect, render
from django.views import View


# Create your views here.
class Signup(View):
    
    def get(self,request):
        return render(request,"signup.html")
    
    def post(self,request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        customer = Customer(first_name = first_name,last_name = last_name,phone = phone,email = email,password = password)

        values = {
            'first_name':first_name,
            'last_name':last_name,
            'phone':phone,
            'email':email
        }
        
        #validation
        
        error_message = self.validateCustomer(customer)

        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('home')
        else:
            data = {
                'error': error_message,
                'values': values
            }
            return render(request,'signup.html',data)


    def validateCustomer(self, customer):
            error_message = None
            if not customer.first_name:
                error_message = "First Name Required!!!"
            elif len(customer.first_name) < 4:
                error_message = 'First name must be 4 char long or more'
            elif not customer.last_name:
                error_message = "Last Name Required!!!"
            elif len(customer.last_name) < 4:
                error_message = 'Last name must be 4 char long or more'
            elif not customer.phone:
                error_message = 'Phone number required!!!'
            elif len(customer.phone) < 10:
                error_message = 'Phone number must be 10 char Long'
            elif len(customer.password) < 6:
                error_message = 'Password must be 6 char long'
            elif len(customer.email) < 5:
                error_message = 'Email must be 5 char long'
            elif not customer.isExists:
                error_message = 'Email Address already registered..!!'

            return error_message
