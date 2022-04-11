from django.urls import path
from .views import home,signup,login,cart
from .views.login import logout
from .views.orders import OrderView
from .views.checkout import CheckOut
from .middlewares.auth import  auth_middleware

urlpatterns = [
    path('', home.Index.as_view(), name='home'),

    path('signup',signup.Signup.as_view(),name = 'signup'),
    path('login',login.Login.as_view(),name = 'login'),
    path('cart',cart.Cart.as_view(),name=  'cart'),
    path('logout',logout, name='logout'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),


]
