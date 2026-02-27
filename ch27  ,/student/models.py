from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

def validate_pin_length(value):
    if len(str(value)) !=6:
        raise ValidationError('the pincode must be exactly 6 digits.')


STATE_CHOICES = [
    ("Andhra Pradesh", "Andhra Pradesh"),
    ("Arunachal Pradesh", "Arunachal Pradesh"),
    ("Assam", "Assam"),
    ("Bihar", "Bihar"),
    ("Chhattisgarh", "Chhattisgarh"),
    ("Goa", "Goa"),
    ("Gujarat", "Gujarat"),
    ("Haryana", "Haryana"),
    ("Himachal Pradesh", "Himachal Pradesh"),
    ("Jharkhand", "Jharkhand"),
    ("Karnataka", "Karnataka"),
    ("Kerala", "Kerala"),
    ("Madhya Pradesh", "Madhya Pradesh"),
    ("Maharashtra", "Maharashtra"),
    ("Manipur", "Manipur"),
    ("Meghalaya", "Meghalaya"),
    ("Mizoram", "Mizoram"),
    ("Nagaland", "Nagaland"),
    ("Odisha", "Odisha"),
    ("Punjab", "Punjab"),
    ("Rajasthan", "Rajasthan"),
    ("Sikkim", "Sikkim"),
    ("Tamil Nadu", "Tamil Nadu"),
    ("Telangana", "Telangana"),
    ("Tripura", "Tripura"),
    ("Uttar Pradesh", "Uttar Pradesh"),
    ("Uttarakhand", "Uttarakhand"),
    ("West Bengal", "West Bengal"),
    ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"),
    ("Chandigarh", "Chandigarh"),
    (
        "Dadra and Nagar Haveli and Daman and Diu",
        "Dadra and Nagar Haveli and Daman and Diu",
    ),
    ("Delhi", "Delhi"),
    ("Jammu and Kashmir", "Jammu and Kashmir"),
    ("Ladakh", "Ladakh"),
    ("Lakshadweep", "Lakshadweep"),
    ("Puducherry", "Puducherry"),
]
# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField(auto_now=False,auto_now_add=False)
    gender=models.CharField(max_length=1)
    locality=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pin=models.PositiveIntegerField(help_text='Enter only 6-digit. ',validators=[validate_pin_length])
    state=models.CharField(choices=STATE_CHOICES,max_length=100)    
    mobile=models.CharField(
        max_length=10,
        help_text='enter 10 digit mobile number.',
        validators=[RegexValidator(regex=r'^\d{10}$')]
    )
    email=models.EmailField(max_length=40)
    job_city=models.CharField(max_length=50)
    profile_image=models.ImageField(upload_to='profileimg',blank=True)
    my_file=models.FileField(upload_to='doc',blank=True)
