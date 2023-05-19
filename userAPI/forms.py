from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


# class UserRegistrationForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email',)


class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email',)