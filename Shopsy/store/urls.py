from django.urls import path
from . import views
from store.views import*

urlpatterns=[
    path('',views.home,name='home'),
    path('search/',views.search,name='search'),
    path('about',views.about,name='about'),
    path('notify',views.notify,name='notify'),
    path('cart_summary',views.cart,name='cart_summary'),
    path('profile',views.profile,name='profile'),
    path('login',views.login_user,name='login'),
    path('logout',views.logout_user,name='logout'),
    path('register',views.register_user,name='register'),
    path('update_password',views.update_password,name='update_password'),
    path('update_user',views.update_user,name='update_user'),
    path('upadate_info',views.update_info,name="update_info"),
    path('product/<int:pk>',views.product,name="product"),
    path('category/<str:foo>',views.category,name="category"),
    path("notifications/", views.notifications, name="notifications"),


]