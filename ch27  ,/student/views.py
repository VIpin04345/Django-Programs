from django.shortcuts import render,redirect
from student.forms import Registration
from student.models import Profile
# Create your views here.
def home(request):
    candidates=Profile.objects.all()
    if request.method=='POST':
        form=Registration(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form=Registration
    return render(request,'student/home.html',{'form':form,'candidates':candidates})


def candidate_details(request,pk):
    candidates=Profile.objects.get(pk=pk)
    return render(request,'student/candidate.html',{'candidate':candidates})