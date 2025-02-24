from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='categoty/')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/')
    banner_image = models.ImageField(upload_to='banner_images/')
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name
    
class CustomUserManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if not email:
            raise ValueError("Please provide email")
        if not username:
            raise ValueError("Please Provide Username")
        email = self.normalize_email(email)
        user = self.model(username=username,email=email)
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self,username,email,password=None):
        user = self.create_user(username,email,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.CharField(unique=True, max_length=20)
    username = models.CharField(unique=True,max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['username'] 

    def __str__(self):
        return f'{self.email}'


            

