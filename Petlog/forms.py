from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import NewPost


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Old Password'})
    )
    new_password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'New Password'})
    )
    new_password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Confirm New Password'})
    )

    class Meta:
        fields = ['old_password', 'new_password1', 'new_password2']


class NewsPostForm(forms.ModelForm):
    title = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Title'})
    )
    content = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control post-description',
                                      'placeholder': 'Description'})
    )

    class Meta:
        model = NewPost
        fields = ['title', 'content', 'image']
