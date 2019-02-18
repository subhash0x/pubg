from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('gamerule/', views.gamerule, name='blog-gamerule'),
    path('googlefcd4e01ee457c3df/', views.seo, name='googlefcd4e01ee457c3df'),
    path('payment/', views.payment, name='blog-payment'),
    path('updateOrder/', views.update_order, name='update-order'),
    path('roominfo/', views.roominfo, name='update-room'),
    path('faq/', views.faq, name='blog-faq'),
    path('howtojoin/', views.howtojoin, name='blog-howtojoin'),
    path('howtoPay/', views.howtoPay, name='blog-howtoPay'),
    path('joininroom/', views.joininroom, name='blog-joininroom'),


]
