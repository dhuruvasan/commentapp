from contextlib import nullcontext
import email
import re
from urllib import request
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import users

# Create your views here.

def home(request):
    return render(request,'index.html')

def signin(request):
    return render(request,'signin.html')

def signup(request):
    return render(request,'signup.html')

def signout(request):
    return render(request,'signout.html')

def signdata(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST.get('password')
        secret=request.POST['code']
        u=users.objects.create(Email=email,password=password,screct=secret)
        u.save()

        messages.success(request,"your account has been successfully created.")

        return redirect('/signin')

    return render(request,"signup")

def signindata(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        emai=users.objects.get(Email=email)
        passs=emai.password
        if password==passs:
            return redirect("comment/emai")
        else:
            return HttpResponse("GO BACK!!! Please check the name and password you entered and try again GO BACK!!!")
            # return render(request,'signin.html')
            