from django.shortcuts import render
from student.forms import Registration
from django.http import HttpResponseRedirect
from student.models import Profile
# Create your views here.
def register(request):
    if request.method=='POST':

        obj=Profile.objects.get(id=1)
        form = Registration(request.POST,instance=obj)
        if form.is_valid():
            # name=form.cleaned_data['name']
            # email=form.cleaned_data['email']
            # password=form.cleaned_data['password']
            # confirm_password=form.cleaned_data['confirm_password']
            # # print('Name:',name)
            # # print('Emsil:',email)
            # # print('Password:',password)
            # # print('Confirm Password:',confirm_password)

            # # user=Profile(name=name,email=email,password=password)
            # # user = Profile(id=1,name=name, email=email, password=password)
            # user = Profile(id=1)
            form.save()
            return HttpResponseRedirect('/success/')
    else:
        form=Registration()
    return render(request,'student/register.html',{'forms':form})

def success(req):
    return render(req,'student/success.html')
