from django import forms
from django.core import validators

def start_with_s(value):
    if value[0]!='s':
        raise forms.ValidationError('Email should start with letter s.')            
class Registration(forms.Form):
    name=forms.CharField(validators=(validators.MinLengthValidator(4),validators.MaxLengthValidator(10)))
    email=forms.EmailField(validators=[start_with_s])
    password=forms.CharField(widget=forms.PasswordInput())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # def clean_name(self):
    #     name_value=self.cleaned_data['name']
    #     if len(name_value)<8:
    #         raise forms.ValidationError('Name can not be less then 8 charecters...!!')
    #     return name_value
    
    # def clean_email(self):
    #     email_value=self.cleaned_data['email']
    #     if len(email_value)<10:
    #         raise forms.ValidationError('email must be atleast 10 charecters...')
    #     return email_value
    
    # def clean_password(self):
    #     password_value=self.cleaned_data.get('password')
    #     if len(password_value)<8:
    #         raise forms.ValidationError('password must be atleast 8 charecters...')
    #     return password_value
    
    
    
    # def clean(self):
    #     cleaned_data=super().clean()
    #     name_value=cleaned_data.get('name')
    #     email_value=cleaned_data.get('email')
    #     password_value=cleaned_data.get('password')
        
    #     if name_value and len(name_value)<8:
    #         self.add_error('name','name can not be less then 8 charecters')
        
    #     if email_value and len(email_value)<10:
    #         self.add_error('email','email value can be 10 or more chaarecters..')
        
    #     if password_value and len(password_value)<8:
    #         self.add_error('password','password must be atleast 8 charecters..')
            
            
    #     return cleaned_data
    
    
    