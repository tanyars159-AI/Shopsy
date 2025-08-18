from django.shortcuts import render,redirect
from .models import Products,Category
from django.db.models import Q
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from store.models import *
from store.forms import *
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

def home(request):
    products=Products.objects.all()
    category=Category.objects.all()
    return render(request,"home.html",{'products':products,'category':category})
def search(request):
    query=request.GET.get('q')
    result=[]
    if query:
        results=Products.objects.filter(
            Q(name__icontains=query)|
            Q(description__icontains=query)
        )
    return render(request,'Search.html',{'query':query,'result':results})
def category(request,foo):
    foo=foo.replace('-',' ')
    try:
        category=Category.objects.get(name=foo)
        products=Products.objects.filter(category=category)
        return render(request,"category.html",{'products':products,'category':category})
    except:
        messages.success(request,("That Category Doesn't Exist"))
        return redirect('home')
def about(request):
    return render(request,'about.html',{})
def notify(request):
    return render(request,'notifications.html',{})
def set(request):
    return render(request,'settings.html',{})
def cart(request):
    return render(request,'cart.html',{})
def login_user(request):
    if request.method=="GET":
        sin=ProjectUserLogInForm()
        return render(request,"LogIn.html",{'sin':sin})
    elif request.method=="POST":
        sin=ProjectUserLogInForm(request.POST)
        if sin.is_valid():
            email=sin.cleaned_data['email']
            password=sin.cleaned_data['password']
            try:
                user=projectUserModel.objects.get(email=email)
                if check_password(password,user.password):

                    request.session['user']=user.username
                    print("Session set for:",user.username)
                    return redirect('/profile')
                else:
                    msg="invalid email or password"
                    print("Passowrd check failed")
                    return render(request,'LogIn.html',{"sin":sin,"msg":msg})
            except projectUserModel.DoesNotExist:
                msg="Invalid email or password"
                return render(request,'LogIn.html',{"sin":sin,"msg":msg})
        else:
            print("Form is not valid. Errors:",sin.errors)
            return redirect('/login')
def signup(request):
    if request.method=="GET":
        sup=ProjectUserSignUpModelForm()
        return render(request,"SignUp.html",{'sup':sup})
    elif request.method=="POST":
        sup=ProjectUserSignUpModelForm(request.POST)
        if sup.is_valid():
            user=sup.save(commit=False)
            user.password=make_password(user.password)
            user.save()
            return redirect('/login')
        else:
            return render(request,'SignUp.html',{'sup':sup})
def profile(request):
    if 'user' in request.session:

        return render(request,"profile.html",{'username':request.session['user']})
    else:
        return redirect('/login')
def logout_user(request):
    if 'user_id' in request.session:
        try:
            user = projectUserModel.objects.get(id=user_id)
            Notification.objects.create(
                user=user,
                message="You have logged out. See you again soon!"
            )

        except projectUserModel.DoesNotExist:
            pass
        del request.session['user_id']
    messages.success(request, "You have been logged out..thanks for visiting")

    return redirect('home')
def product(request,pk):
    product=Products.objects.get(id=pk)
    return render(request,'product.html',{'product':product})

