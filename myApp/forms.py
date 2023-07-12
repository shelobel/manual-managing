from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Manual


class ManualForm(forms.ModelForm):
    class Meta:
        model = Manual
        fields = '__all__'

class ManualUpdateForm(forms.ModelForm):
    class Meta:
        model = Manual
        fields = '__all__'
        exclude = ['title']

# class materialForm(ModelForm):
#     class Meta:
#         model = material
#         fields = '__all__'
#         exclude = ['manual']
        

# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username','email','password1','password2']