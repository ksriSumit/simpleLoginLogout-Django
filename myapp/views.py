from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        verifyPassword = request.POST['verifypassword']
        email = request.POST['email']
        if password==verifyPassword:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Exist')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                redirect('login')
        else:
            messages.info(request,'Password Didnot Match')
            return redirect('register')
    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Username/Password")
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def index(request):
    return render(request,'index.html')