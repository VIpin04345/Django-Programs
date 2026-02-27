from django import forms
from student.models import Profile

GENDER_CHOICES=(
    ('M','Male'),
    ('F','Female'),
    ('O','Other')
)

JOB_CITY_CHOICES = [
    ("Bengaluru", "Bengaluru"),
    ("Mumbai", "Mumbai"),
    ("Hyderabad", "Hyderabad"),
    ("Pune", "Pune"),
    ("Chennai", "Chennai"),
    ("Delhi", "Delhi"),
    ("Noida", "Noida"),
    ("Gurugram", "Gurugram"),
    ("Ahmedabad", "Ahmedabad"),
    ("Kolkata", "Kolkata"),
]

class Registration(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICES)
    job_city=forms.MultipleChoiceField(choices=JOB_CITY_CHOICES,widget=forms.CheckboxSelectMultiple,label='Preferred Job Cities',help_text='Select One Or More Cities Where you Prefer To Work')
    class Meta:
        model=Profile
        fields=['name','dob','gender','locality','city','pin','state','mobile','email','job_city','profile_image','my_file']
        labels={
            'name':'Full Name:',
            'dob':'Date of Birth:',
            'gender':'Gender:',
            'locality':'Locality:',
            'pin':'Pincode:',
            'mobile':'Mobile Number:',
            'city':'City:',
            
        }
        help_texts={
            'profile_image':'Optional: Upload a profile image.',
            'my_file':'Optional: Attach any additional document (PDF,DOCX, etc.)',
            'mobile':'enter 10 digits mobile number'
        }        

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "dob": forms.DateInput(attrs={"class": "form-control",'id':'datepicker','type':'date'}),
            'gender':forms.RadioSelect(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control','placeholder':'write your locality.'}),
            'city':forms.TextInput(attrs={'class':'form-control','placeholder':'write your city name.'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-select'}),
            'mobile':forms.TextInput(attrs={'class':'form-control','placeholder':'enter 10 digits mobile number.'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            
            
        }
