from django.contrib import admin
from user.models import User, Post, Seguidor, Comment
from django.contrib.auth.admin import UserAdmin


class PostAdmin(admin.ModelAdmin):
    ...


class UserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password', 'email', 'photo'),
        }),
    )
admin.site.register(User,UserAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Seguidor)
admin.site.register(Comment)
