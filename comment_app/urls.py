from django import views
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('',views.signin, name="home"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('forget',views.forget,name="forget"),
    path('forgetpass',views.forgetpass,name="forgetpass"),
    path('signdata',csrf_exempt(views.signdata),name="signdata"),
    path('logins',views.signindata,name="logins"),
    path('comment/<id>',views.comment,name="comment"),
    path('commented',views.commented,name="commented"),
    path('comment/commendin/<id>',views.commendin,name="commentin")
]