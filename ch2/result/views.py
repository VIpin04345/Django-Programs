from django.shortcuts import render,httpresponse

# Create your views here.
def hello(request):
    return httpresponse('hello')