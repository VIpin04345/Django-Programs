from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def course1(req):
    return HttpResponse(' heading of course1 app')

def course2(req):
    return HttpResponse('heading of course2 app')
