from django.shortcuts import render
from .models import Products
# Create your views here.
def home(request):
    products=Products.objects.all()
    return render(request,"home.html",{'products':products})
def about(request):
    return render(request,'about.html',{})
def notify(request):
    return render(request,'notifications.html',{})
def profile(request):
    return render(request,'profile.html',{})
def set(request):
    return render(request,'settings.html',{})
def cart(request):
    return render(request,'cart.html',{})
