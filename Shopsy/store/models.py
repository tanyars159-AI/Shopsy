from django.db import models
import datetime
 
# Create your models here.
#Categories for models
class Category(models.Model):
    name=models.CharField(max_length=50)
    class Meta:
        verbose_name_plural='categories'
    def __str__(self):
        return self.name
#Customer  
class Customer(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
"User"
class projectUserModel(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=128)
    
    def __str__(self):
        return self.username+' '+self.email
#All of our products
class Products(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(default=0,decimal_places=2,max_digits=7)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description=models.CharField(max_length=200,default='',blank=True,null=True)
    image=models.ImageField(upload_to='uploads/products/')
    def __str__(self):
        return f"{self.name}"
#Customer Orders
class Order(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    address=models.CharField(max_length=100,default='',blank=True)
    phone=models.CharField(max_length=20,default='',blank=True)
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.product
    
    
class Notification(models.Model):
    user = models.ForeignKey('projectUserModel', on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.message[:30]}"
