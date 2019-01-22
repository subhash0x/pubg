from django.urls import path,include
from paytm.views import home,payment,response
from django.conf.urls import url, include
from . import views

urlpatterns = [

   path('',views.home, name='paytm-home'),
   path('payment/',views.payment, name='paytm-payment'),
   path('response/',views.response, name='paytm-response'),
]



# from django.conf.urls import include, url
#
#
# urlpatterns = [
#     # Examples:
#     url(r'^$', 'paytm.views.home', name='home'),
#     url(r'^payment/', 'paytm.views.payment', name='payment'),
#     url(r'^response/', 'paytm.views.response', name='response'),
# ]
