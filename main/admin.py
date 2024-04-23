from django.contrib import admin
from .models import *
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserDInline(admin.StackedInline):
    model = UserUpdate
    can_delete = False
    verbose_name_plural = 'User Extends'


class UserAdmin(BaseUserAdmin):
    inlines = (UserDInline,)
    list_display = ('username','email','last_name','first_name', )
    search_fields = ('username' , 'last_name' , 'first_name')

@admin.register(Connected_users)
class Connected_usersAdmin(admin.ModelAdmin ):
    model = Connected_users

admin.site.unregister(User)
admin.site.register(User, UserAdmin)