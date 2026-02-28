from django.shortcuts import render
from django.http import HttpResponseRedirect
from student.forms import Registration
# Create your views here.

def register(request):
    if request.method=='POST':
        form=Registration(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            print('Name:',name)
            print('Email:',email)
            print('Password:',password)
            return HttpResponseRedirect('/success/')
    else:
        form=Registration()
    return render(request,'student/register.html',{'forms':form})


def success(req):
    return render(req,'student/success.html')
