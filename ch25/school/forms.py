from django import forms
from school.models import Profile
class Stu_registration(forms.ModelForm):
    class Meta:
        model=Profile 
        fields=['student_name','email','password']
        labels=[{'student_name':'Student Name','email':'Email','password':'Password'}]
        widgets=[{'password':forms.PasswordInput()}]


class Tea_registration(Stu_registration):
    class Meta(Stu_registration.Meta):
        model = Profile
        fields = ["teacher_name", "email", "password"]
        labels = [
            {"teacher_name": "Teacher Name", "email": "Email", "password": "Password"}
        ]
        widgets = [{"password": forms.PasswordInput()}]
