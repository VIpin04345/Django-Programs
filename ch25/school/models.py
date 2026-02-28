from django.db import models

# Create your models here.
class Profile(models.Model):
    teacher_name=models.CharField(max_length=200)
    student_name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=200)