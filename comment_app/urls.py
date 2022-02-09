from django import views
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('',views.signin, name="home"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name="signout"),

    path('signdata',csrf_exempt(views.signdata),name="signdata"),
    path('logins',views.signindata,name="logins"),
]