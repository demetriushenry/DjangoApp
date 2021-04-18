from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


class AppUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = '__all__'


class AppUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = '__all__'
