from django.contrib import admin
from .models import MenuCategory, Menu, Logger
from django.contrib.auth.models import User 
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(MenuCategory)
admin.site.register(Menu)
admin.site.register(Logger)
admin.site.unregister(User)

@admin.register(User)
class NewAdmin(UserAdmin): 
    def get_form(self, request, obj=None, **kwargs): 
        form = super().get_form(request, obj, **kwargs) 
        is_superuser = request.user.is_superuser 

        if not is_superuser: 
            form.base_fields['username'].disabled = True 

        return form