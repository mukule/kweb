from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from .forms import CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    model = get_user_model()

    def save_model(self, request, obj, form, change):
        password = form.cleaned_data.get('password1')
        if password:
            obj.password = make_password(password)
        super().save_model(request, obj, form, change)

admin.site.register(get_user_model(), CustomUserAdmin)
