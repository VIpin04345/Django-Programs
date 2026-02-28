from django import forms
from student.models import Profile
from django.core import validators
# class Registration(forms.Form):
#     name=forms.CharField()
#     email=forms.EmailField()
#     password=forms.CharField(widget=forms.PasswordInput)


class Registration(forms.ModelForm):
    name=forms.CharField(max_length=30)
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=Profile
        # fields=['name','email','password']
        # fields='__all__'
        exclude=['email']
        labels={'name':'Full Name','email':'Your Email'}
        widgets={
            "password":forms.PasswordInput(),
            'name':forms.TextInput(attrs={'class':'myclass','placeholder':'write your name here'})
        }
        error_messages={
            'email':{'required':'Email is required'}
            
        }
        