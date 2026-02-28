from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello2(req):
    var='app 2 heading 2'
    return HttpResponse(var)

def yes2(req):
    return HttpResponse('app 2 response 2' )
