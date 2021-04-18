from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import AppUserChangeForm, AppUserCreationForm
from .models import User


class AppUserAdmin(UserAdmin):
    add_form = AppUserCreationForm
    form = AppUserChangeForm
    model = User
    list_display = ('name', 'birthday', 'cpf', 'is_staff', 'is_active',)
    list_filter = ('name', 'birthday', 'cpf', 'is_staff', 'is_active',)
    ffieldsets = (
        (None, {'fields': ('name', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser', 'groups',
                'user_permissions'
            ),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined', 'birthday')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'name',
                'birthday',
                'cpf',
                'cep',
                'street',
                'neighborhood',
                'city',
                'state',
                'password1',
                'password2',
                'is_staff',
                'is_active'
            )
        }),
    )
    search_fields = ('name',)
    ordering = ('name',)


admin.site.register(User, AppUserAdmin)
