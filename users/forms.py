from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile



class UserRegisterForm(UserCreationForm):
    OPTIONS = [
            ('M', 'male'),
            ('F', 'female')
            ]
    email = forms.EmailField()
    sex = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect(), label='jensiyat')

    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2', 'sex']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField() 

    class Meta:
        model = User 
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
