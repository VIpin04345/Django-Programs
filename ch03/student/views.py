from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse(('hello Django'))

def operation(request):
    sum=364+2667
    return HttpResponse(sum)

def html(request):
    return HttpResponse('<h1>Shubham</h1>')

def var(request):
    var='Shubham yadav'
    return HttpResponse(var)
