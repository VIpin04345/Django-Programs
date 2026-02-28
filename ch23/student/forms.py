from django import forms

class Registration(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    age=forms.IntegerField()
    city=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())