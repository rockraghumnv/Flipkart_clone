from django.shortcuts import render,HttpResponse
from .models import Product,Category,BaseUserManager,CustomUser
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request,'index.html',{'MEDIA_URL':'/media/','products':products})

def user_login(request):
    if request.method == 'POST':
       email = request.POST.get('email')
       password = request.POST.get('password')

       user = authenticate(request,email=email,password=password)
       if user is not None:
           login(request, user)
           return HttpResponse(f"Logged in {user}")
       else:
           return HttpResponse("Incorrect Username or password")
    return render (request,'login.html')

def signup(request):
    
    if request.method == 'POST':
        print("POST")
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
       #print(email,username,password)
        
        user = CustomUser.objects.create_user(username=username,email=email,password=password)
        #print(user)
        return HttpResponse(f"registered user:{user}")

    return render(request,'signup.html')

