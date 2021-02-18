from django import forms
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from.models import CustomUser
from django import forms
from django.core.files import File

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=CustomUser
        fields=('username','email','age')
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields=('username','email','age')

