from django.shortcuts import render
from student.forms import Registration
from django.http import HttpResponseRedirect
# Create your views here.
def register(request):
    if request.method=='POST':
        # print(request.POST)
        # print(request.POST['name'])
        # print(request.POST["email"])
        # print(request.POST["age"])
        # print(request.POST["city"])
        form=Registration(request.POST)
        # print(form)
        # print(form.is_valid())
        if form.is_valid():
            # print(form.cleaned_data)
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            age=form.cleaned_data['age']
            city=form.cleaned_data['city']
            print('name=', name)
            print('email=',email)
            print('age=',age)
            print('city=',city)
            return HttpResponseRedirect('/success/')
    else:
        form=Registration()
    return render(request,'student/register.html',{'forms':form})


def success(req):
    return render(req,'student/success.html')