from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def home(request):
    data=Post.objects.all()
    return render(request,'index.html',{'posts':data})

def page1(request):
    return render(request,'page1.html')
def register(request):
    return render(request,'register.html')
def addUser(request):
    Username=request.POST['Username']
    First=request.POST['First']
    Last=request.POST['Last']
    Email=request.POST['Email']
    Password=request.POST['Password']
    RePassword=request.POST['RePassword']
    
    if Password != RePassword:
        messages.info(request,'Password incorrect')
        return redirect('/register')
    elif User.objects.filter(username=Username):
        messages.info(request,'Username already use')
        return redirect('/register')
    elif User.objects.filter(email=Email):
        messages.info(request,'Email already use')
        return redirect('/register')
    else:
        user=User.objects.create_user(
            username=Username,
            password=Password,
            email=Email,
            first_name=First,
            last_name=Last,
            )
        user.save()
        return redirect('/')
def loginform(request):
    return render(request,'loginform.html')
def login(request):
    Username=request.POST['Username']
    Password=request.POST['Password']
    
    user=auth.authenticate(username=Username,password=Password)
    
    if user is not None:
        auth.login(request,user)
        return redirect('/')
    else:
        messages.info(request,'No info')
        return redirect('/loginform')
def logout(request):
    auth.logout(request)
    return redirect('/')