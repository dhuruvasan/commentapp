from contextlib import nullcontext
import email
import re
from urllib import request
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import comm, users

# Create your views here.

def home(request):
    return render(request,'index.html')

def signin(request):
    return render(request,'signin.html')

def signup(request):
    return render(request,'signup.html')

def forget(request):
    return render(request,'forgetpass.html')

def forgetpass(request):
    if request.method=="POST":
        email=request.POST.get('email')
        screct=request.POST.get('code')
        try:
            use=users.objects.get(Email=email)
            if screct==use.screct:
                passw=use.password
                return render(request,"password.html",{'passw':passw})
            else:
                return HttpResponse("GO BACK!!! Please check the email and scerect you entered and try again GO BACK!!!")
        except:
            return HttpResponse("GO BACK!!! Please check the email and scerect you entered and try again GO BACK!!!")

def signdata(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST.get('password')
        secret=request.POST['code']
        try:
            u=users.objects.create(Email=email,password=password,screct=secret)
            u.save()

            messages.success(request,"your account has been successfully created.")

            return redirect('/signin')
        except:
            return HttpResponse("GO BACK!!! The Entered email is alredy taken GO BACK!!!")

    return render(request,"signup")

def signindata(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            emai=users.objects.get(Email=email)
            passs=emai.password
            id=emai.id
            iid=str(id)
            if password==passs:
                return redirect("comment/"+iid)
            else:
                return HttpResponse("GO BACK!!! Please check the Email and password you entered and try again GO BACK!!!")
        except:
            return HttpResponse("GO BACK!!! Please check the Email and password you entered and try again GO BACK!!!")
            # return render(request,'signin.html')

def comment(request,id):
    use=users.objects.get(id=id)
    comme=comm.objects.filter(id=id)
    commd=comm.objects.all()

    return render(request,"comment.html",{'use':use,'commd':commd})

def commented(request):
    if request.method=="POST":
        comment=request.POST.get('comment')
        id=request.POST.get('id')
        use=users.objects.get(id=id)
        email=use.Email
        print(email)
        cm=comm.objects.create(idname=id,Email=email,comment=comment)
        cm.save()
        iid=str(id)
        return redirect("comment/"+iid)
    else:
        return HttpResponse("GO BACK!!!error try again GO BACK!!!")

def commendin(request,id):
    use=users.objects.get(id=id)
    commd=comm.objects.filter(idname=id)
    return render(request,"commendin.html",{'use':use,'commd':commd})