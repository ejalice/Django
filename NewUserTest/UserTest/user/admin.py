from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

# Register your models here.
class UserAdmin(UserAdmin):
    list_display = ('email', 'password', 'is_staff')
    search_fields = ('email', 'password')
    readonly_fields = ('id',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ('email',)

admin.site.register(User, UserAdmin)

# admin.site.register(User)
