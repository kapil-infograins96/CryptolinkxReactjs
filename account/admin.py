from django.contrib import admin
from .models import Custom_User


# Register your models here.

class Custom_userAdmin(admin.ModelAdmin):
    model =Custom_User
    list_desplay = ['email', 'username', 'phone', 'is_active', 'is_superuser'] 


admin.site.register(Custom_User,Custom_userAdmin)