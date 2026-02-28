from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello1(req):
    var='app 1 heading 1'
    return HttpResponse(var)

def yes1(req):
    var='app 1 response 1 '
    return HttpResponse(var)
