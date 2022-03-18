from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm
from .models import User,Company


class CustomUserAdmin(UserAdmin):
   
    add_form = CustomUserCreationForm
    model = User
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )
    

admin.site.register(User, CustomUserAdmin)
admin.site.register(Company)