from django import forms
from django.core import validators

class Registration(forms.Form):
    error_css_class='mymycss'
    required_css_class='yourcss'
    name=forms.CharField(error_messages={'required':'Name field is mendetory..!!'})
    email = forms.EmailField(error_messages={"required": "Email field is mendetory..!!"})
    password = forms.CharField(widget=forms.PasswordInput(),error_messages={'required':'Password is required..!!'})
