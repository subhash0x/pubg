from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('gamerule/', views.gamerule, name='blog-gamerule'),
    path('payment/', views.payment, name='blog-payment'),
    path('updateOrder/', views.update_order, name='update-order'),

]
