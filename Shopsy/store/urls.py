from django.urls import path
from . import views
from store.views import*

urlpatterns=[
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('notify',views.notify,name='notify'),
    path('set',views.set,name='set'),
    path('cart',views.cart,name='cart'),
    path('profile',views.profile,name='profile')


]