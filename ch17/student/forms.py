from django import forms

class Registration(forms.Form):
    first_name=forms.CharField()
    last_name=forms.CharField()
    email=forms.EmailField()
    age=forms.IntegerField(help_text='enter your age')
    city=forms.CharField()
    
class Address(forms.Form):
    city=forms.CharField()
    state=forms.CharField()
    pincode=forms.IntegerField()
    
    
class Login(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())
    key=forms.CharField(widget=forms.HiddenInput())