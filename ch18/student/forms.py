from django import forms
from django.core.validators import MinLengthValidator , RegexValidator


gender_choices=[
    ('M','male'),
    ('F','female'),
    ('O','other')]

intrest_choices=[
    ("p",'playing'),
    ('D','dancing'),
    ('S','singing')
]
class Demo_form(forms.Form):

    # name=forms.CharField()
    # email=forms.EmailField()
    # pin_code=forms.IntegerField()
    # D_O_B=forms.FloatField()

    # appointment_date=forms.DateField()
    # appointment_time=forms.TimeField()
    # appointment_date_time=forms.DateTimeField()
    # is_subscribed=forms.BooleanField()
    # is_agree=forms.NullBooleanField()

    # gender=forms.ChoiceField(choices=gender_choices)
    # intrest=forms.MultipleChoiceField(choices=intrest_choices)

    # website=forms.URLField()
    # image=forms.ImageField()
    # resume=forms.FileField()

    # password=forms.CharField(widget=forms.PasswordInput())
    # mobile_no=forms.RegexField(regix=r'^/?/(6,15)')
    # ip_address=forms.GenericIPAddressField()
    # slug=forms.SlugField()
    # rating=forms.DecimalField()

    # name=forms.CharField(
    #     label='Full Name',
    #     help_text='Enter your name',
    #     initial='Shubham',
    #     label_suffix=":",
    #     required=True,
    #     max_length=100,
    #     validators=[MinLengthValidator(3)]

    # )
    # email=forms.EmailField(
    #     label="Email",
    #     disabled=True,
    # )
    # pin_code=forms.IntegerField(
    #     min_value=111111,
    #     max_value=999999,
    #     error_messages={
    #         'min_value':'pin code must be atleast 6 digit',
    #         'max_value':'pin code can be atmost 6 digits'
    #     }
    # )
    # D_O_B=forms.FloatField(
    #     label='date of birth',
    #     min_value=0
    # )

    # appointment_date=forms.DateField(
    #     label='Appointment Time',
    #     required=True,
    #     help_text='enter your dob in dd:mm:yyyy'
    # )
    # appointment_time=forms.TimeField(
    #     label='Appointment time',
    #     required=True
    # )
    # appointment_date_time=forms.DateTimeField(
    #     label='Appointment Datetime',
    #     required=True
    # )
    # is_subscribed=forms.BooleanField(
    #     label='Is Subscribed',
    #     required=True
    # )
    # is_agree=forms.NullBooleanField(
    #     label='Agree Terms',
    #     required=True
    # )

    # gender=forms.ChoiceField(choices=gender_choices,label='Gender',required=True)
    # intrest=forms.MultipleChoiceField(choices=intrest_choices,label='Intrests',required=True)

    # website=forms.URLField(label='Web Link',
    #     required=True)
    # image=forms.ImageField(label='Passport Image',
    #     required=True)
    # resume=forms.FileField(label='Resume',
    #     required=True)

    # password=forms.CharField(
    #     widget=forms.PasswordInput(),label='Password',help_text='Enter your password here',
    #     max_length=50,min_length=8,
    #     error_messages={
    #         'min_length':'password must be atleast 8 charecters',
    #         'max_length':'password must be atmost 50 charecters'
    #     }
    #     )
    # mobile_no=forms.RegexField(
    #     regex=r'^\+?1?\d{9,15}$',
    #     label='Phone Number',
    #     error_messages={'invalid':'enter a valid phone number'}
    #     )
    # ip_address=forms.GenericIPAddressField(
    #     localize=True,
    #     protocol='both',
    #     label='Ip_Address',
    #     unpack_ipv4=False
    # )
    # slug=forms.SlugField(label='SLUG',required=True,max_length=50)
    # rating=forms.DecimalField(
    #     label='Rating',
    #     min_value=0,
    #     max_value=10,
    #     initial=5.0,
    #     localize= True
    # # )

    # name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'type here','class':'mycss'}),
    #     label="Full Name",
    #     help_text="Enter your name",
    #     initial="Shubham",
    #     label_suffix=":",
    #     required=True,
    #     max_length=100,
    #     validators=[MinLengthValidator(3)],
    # )
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'type here...'}),
    #     label="Email",
    #     disabled=True,
    # )
    # pin_code = forms.IntegerField(widget=forms.HiddenInput(attrs={'placeholder':'type here..'}),
    #     min_value=111111,
    #     max_value=999999,
    #     error_messages={
    #         "min_value": "pin code must be atleast 6 digit",
    #         "max_value": "pin code can be atmost 6 digits",
    #     },
    # )
    # D_O_B = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'type here.....'}),label="date of birth", min_value=0)

    # appointment_date = forms.DateField(
    #     widget=forms.DateInput(attrs={"type": "date", "placeholder": "type here..."}),
    #     label="Appointment Time",
    #     required=True,
    #     help_text="enter your dob in dd:mm:yyyy",
    # )
    # appointment_time = forms.TimeField(widget=forms.TimeInput(attrs={'type':'time','placeholder':'typr here'}),label="Appointment time", required=True)
    # appointment_date_time = forms.DateTimeField(
    #     widget=forms.DateTimeInput(
    #         attrs={"type": "datetime-local", "placeholder": "enter your time"}
    #     ),
    #     label="Appointment Datetime",
    #     required=True,
    # )
    # blog_content=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'enter the content'}))
    # is_subscribed = forms.BooleanField(widget=forms.CheckboxInput(attrs={'placeholder':'type here...'}),
    # label="Is Subscribed", required=True)
    # is_agree = forms.NullBooleanField(widget=forms.NullBooleanSelect(attrs={'placeholder':'type here...'}),label="Agree Terms", required=True)

    # gender = forms.ChoiceField(widget=forms.Select(attrs={'placeholder':'enter your gender...'}),choices=gender_choices, label="Gender", required=True)
    # intrest = forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={'placeholder':'enter your intrest...'}),
    #     choices=intrest_choices, label="Intrests", required=True
    # )

    # website = forms.URLField(widget=forms.URLInput(),label="Web Link", required=True)
    # image = forms.ImageField(label="Passport Image", required=True,widget=forms.FileInput(attrs={'placeholder':'submit your image'}))
    # resume = forms.FileField(label="Resume", required=True,widget=forms.ClearableFileInput(attrs={'placeholder':'enter your resume'}))

    # password = forms.CharField(
    #     widget=forms.PasswordInput(),
    #     label="Password",
    #     help_text="Enter your password here",
    #     max_length=50,
    #     min_length=8,
    #     error_messages={
    #         "min_length": "password must be atleast 8 charecters",
    #         "max_length": "password must be atmost 50 charecters",
    #     },
    # )
    # mobile_no = forms.RegexField(
    #     regex=r"^\+?1?\d{9,15}$",
    #     label="Phone Number",
    #     error_messages={"invalid": "enter a valid phone number"},
    # )
    # ip_address = forms.GenericIPAddressField(widget=forms.TextInput(attrs={'placeholder':'enter your ip_address'}),
    #     localize=True, protocol="both", label="Ip_Address", unpack_ipv4=False
    # )
    # slug = forms.SlugField(label="SLUG", required=True, max_length=50,widget=forms.TextInput(attrs={'placeholder':'enter your slug'}))
    # rating = forms.DecimalField(widget=forms.NumberInput(attrs={21'placeholder':'enter your rating.'}),
    #     label="Rating", min_value=0, max_value=10, initial=5.0, localize=True
    # )
    
    



