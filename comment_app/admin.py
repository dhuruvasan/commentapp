from django.contrib import admin
from .models import *
from comment_app.models import users

admin.site.register(users)
# Register your models here.
