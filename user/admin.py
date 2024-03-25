from django.contrib import admin
from user.models import User, Post
from django.contrib.auth.admin import UserAdmin


class PostAdmin(admin.ModelAdmin):
    ...
admin.site.register(User,UserAdmin)
admin.site.register(Post,PostAdmin)
