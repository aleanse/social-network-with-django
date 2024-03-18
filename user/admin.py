from django.contrib import admin
from user.models import User, Post
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(User,UserAdmin)
