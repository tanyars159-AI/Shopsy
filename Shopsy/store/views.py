from django.shortcuts import render,redirect
from .models import Products,Category
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from store.models import *
from store.forms import *
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.
def home(request):
    products=Products.objects.all()
    category=Category.objects.all()
    return render(request,"home.html",{'products':products,'category':category})
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
    if request.method == "POST":
        sin = ProjectUserLogInForm(request.POST)
        if sin.is_valid():
            email = sin.cleaned_data['email']
            password = sin.cleaned_data['password']
            try:
                user = projectUserModel.objects.get(email=email)
                if check_password(password, user.password):
                    request.session['user_id'] = user.id
                    print("Session set for:", user.username)
                    Notification.objects.create(
                        user=user,
                        message="You have successfully logged into your account."
                    )
                    return redirect('/profile')
                else:
                    msg = "Invalid email or password"
                    return render(request, 'LogIn.html', {"sin": sin, "msg": msg})
            except projectUserModel.DoesNotExist:
                msg = "Invalid email or password"
                return render(request, 'LogIn.html', {"sin": sin, "msg": msg})
    else:
        sin = ProjectUserLogInForm()
    return render(request, "LogIn.html", {'sin': sin})


def profile(request):
    user_id = request.session.get('user_id')
    if user_id:
        try:
            user = projectUserModel.objects.get(id=user_id)
            return render(request, "profile.html", {"user": user})
        except projectUserModel.DoesNotExist:
            return redirect('/login')
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
            Notification.objects.create(
                user=user,
                message="Welcome to our store! 🎉"
            )
            return redirect('/login')
        else:
            return render(request,'SignUp.html',{'sup':sup})


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

from django.contrib.auth.hashers import check_password, make_password

def change_password(request):
    if request.method == "POST":
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']

        user_id = request.session.get('user_id')
        if not user_id:
            return redirect('/login')

        try:
            user = projectUserModel.objects.get(id=user_id)
            if check_password(old_password, user.password):
                user.password = make_password(new_password)
                user.save()
                Notification.objects.create(
                user=user,
                message="Welcome Back! 🎉."
                )
                messages.success(request, "Password updated successfully!")
                return redirect('/profile')
            else:
                messages.error(request, "Old password is incorrect.")
                return redirect('/settings')
        except projectUserModel.DoesNotExist:
            return redirect('/login')
        
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


def product(request,pk):
    product=Products.objects.get(id=pk)
    return render(request,'product.html',{'product':product})

