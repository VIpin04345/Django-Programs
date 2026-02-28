from django.shortcuts import render
from student.models import Profile

# Create your views here.
def register(req):
    students=Profile.objects.all()
    return render(req,'student/register.html',{'students':students})

def login(req):
    stu=Profile.objects.get(id=102)
    return render(req,'student/single.html',{'students':stu})