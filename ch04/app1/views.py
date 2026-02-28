from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello1(request):
    return HttpResponse('<h1> this is the first heading of app1 </h1>')


def parah1(request):
    return HttpResponse('<p> this is the first parah of app1</p>')