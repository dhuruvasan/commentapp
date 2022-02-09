from django.contrib import admin
from .models import *
from comment_app.models import users

admin.site.register(users)
admin.site.register(comm)
# Register your models here.
