from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from todo.models import CustomUser


class CreateUserForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ["email"]


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ["email"]
