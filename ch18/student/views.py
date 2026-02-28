from django.shortcuts import render
from student.forms import Demo_form
# Create your views here.
def demo_form(req):
    fm=Demo_form()
    return render(req,'student/demo.html',{'form':fm})
