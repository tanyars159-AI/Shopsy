from django.shortcuts import render,redirect
from .models import Products,Category
from django.db.models import Q
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from store.models import *
from store.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from payment.forms import ShippingForm
from payment.models import ShippingAddress
from django import forms
from django.contrib.auth.hashers import check_password, make_password

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
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.success(request,("There was an error,please try again"))
            return redirect('login')
    else:  
        return render(request,"LogIn.html")
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out..thanks for visiting")
    return redirect('home')

def profile(request):
    user_id = request.session.get('user_id')
    if user_id:
        try:
            user = projectUserModel.objects.get(id=user_id)
            return render(request, "profile.html", {"user": user})
        except projectUserModel.DoesNotExist:
            return redirect('/login')
    return redirect('/login')
def update_user(request):
    if request.user.is_authenticated:
        current_users=User.objects.get(id=request.user.id)
        user_form=UpdateUserForm(request.POST or None,instance=current_users)
        if user_form.is_valid():
            user_form.save()
            login(request,current_users)
            messages.success(request,("User has been updated!!"))
            return redirect('home')
        return render(request,'settings.html',{'user_form':user_form})
    else:
        messages.success(request,"You must be logged in to access that page")
        return redirect('home')

def update_info(request):
    if request.user.is_authenticated:
        #get current user 
        current_users=Profile.objects.get(user__id=request.user.id)
        # yaha pe uper error ho skta h
        # get original user's shipping info
        shipping_user=ShippingAddress.objects.get(user__id=request.user.id)
        # get original user form
        form=UserInfoForm(request.POST or None,instance=current_users)
        # get shipping user form
        shipping_form=ShippingForm(request.POST or None,instance=shipping_user)
        if form.is_valid() or shipping_form.is_valid():
            form.save()
            shipping_form.save()
            # login(request,current_users)
            messages.success(request,("Your Info has been updated!!"))
            return redirect('home')
        return render(request,'settings.html',{'form':form,'shipping_form':shipping_form})
    else:
        messages.success(request,"You must be logged in to access that page")
        return redirect('home')
def update_password(request):
    if request.user.is_authenticated:
        current_user=request.user
        if request.method=='POST':
            form=ChangePasswordForm(current_user,request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Your Password Has Been Updated!Please Log In Again...")
                login(request,current_user)
                # update_session_auth_hash(request,current_user)
                return redirect('login')
            else:
                for error in list(form.errors.values()):
                    messages.error(request,error)
                    return redirect('set')

        else:
            form=ChangePasswordForm(current_user)
            return render(request,"settings.html",{'form':form})
    else:
        messages.success(request,"You must be logged in update this section")
        return redirect('/set')
    
def notifications(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('/login')

    try:
        user = projectUserModel.objects.get(id=user_id)
        notifications = Notification.objects.filter(user=user).order_by('-created_at')
    except projectUserModel.DoesNotExist:
        return redirect('/login')

    return render(request, "notifications.html", {"notifications": notifications})
def register_user(request):
    form=SignUpForm()
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,("You Have Registered Succesfully"))
            return redirect('home')
        else:
            messages.success(request,("OOps there was a problem please try again later"))
            return redirect('register')
    else:
        return render(request,'Register.html',{'form':form})

def product(request,pk):
    product=Products.objects.get(id=pk)
    return render(request,'product.html',{'product':product})

