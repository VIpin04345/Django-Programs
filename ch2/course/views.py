from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('HOME PAGE')
def learn_dj(request):
    return HttpResponse('Hello Django')

def learn_py(request):
    return HttpResponse('<h1>Hello Python</h1>')

def learn_var(request):
    a='<h3>Hello variables</h3>'
    return HttpResponse(a)

def learn_math(request):
    a=10+10
    b=20-10
    return HttpResponse(f'{a} and {b}')
def learn_for(request):
    a='shubham'
    return HttpResponse(f'hello how are you  {a}')