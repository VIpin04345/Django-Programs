from django.db import models

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField(max_length=200)
    age=models.IntegerField()
    city=models.CharField(max_length=200)
    
    
    def __str__(self):
        return str(self.id)
    
class Result(models.Model):
    marks=models.IntegerField()
    grade=models.CharField(max_length=2)
    result=models.CharField(max_length=200)
    def __str__(self):
        return str(self.id)