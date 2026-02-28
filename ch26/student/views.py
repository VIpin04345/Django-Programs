from django.shortcuts import render

# Create your views here.
def data(req):
    context={'data':'i am the best . i am the programmer . i am not a human . i am so happy to learn djando'}
    return render(req,'student/home.html',context)