from django.urls import path
from . import views
from store.views import*

urlpatterns=[
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('notify',views.notify,name='notify'),
    path('set',views.set,name='set'),
    path('cart',views.cart,name='cart'),
    path('profile',views.profile,name='profile'),
    path('login',views.login_user,name='login'),
    path('logout',views.logout_user,name='logout'),
    path('signup',views.signup,name="signup"),
    path('product/<int:pk>',views.product,name="product"),
    path('category/<str:foo>',views.category,name="category"),
    path("change_password", views.change_password, name="change_password"),
    path("notifications/", views.notifications, name="notifications"),


]