from django.shortcuts import render
from django.http import HttpResponseRedirect
from student.forms import Registration
from student.models import  Profile
# Create your views here.
def register(request):
    if request.method=='POST':
        form=Registration(request.POST)
        if form.is_valid():
            nm=form.cleaned_data['name']
            em=form.cleaned_data['email']
            ag=form.cleaned_data['age']
            ct=form.cleaned_data['city']
            pw=form.cleaned_data['password']
            # user=Profile(name=nm , email=em , age=ag , city=ct , password=pw)
            # user = Profile(id=104, name=nm, email=em, age=ag, city=ct, password=pw)
            user = Profile(id=104)
            user.delete()
            return HttpResponseRedirect('/success/')    
    else:
        form=Registration()
    return render(request,'student/register.html',{'forms':form})

def success(req):
    return render(req,'student/success.html')
