from django.shortcuts import render
from django.http import HttpResponseRedirect
from school.models import Profile
from school.forms import Stu_registration , Tea_registration
# Create your views here.
def stu_register(request):
    if request.method=='POST':
        form=Stu_registration(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/sch/success/')
    else:
        form=Stu_registration()
    return render(request,'school/student_reg.html',{'forms':form})


def tea_register(request):
    if request.method=='POST':
        form=Tea_registration(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/sch/success/")
    else:
        form = Tea_registration()
    return render(request, "school/teacher_reg.html", {"forms": form})


def success(req):
    return render(req,'school/success.html')