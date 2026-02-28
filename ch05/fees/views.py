from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def fees1(req):
    return HttpResponse(" heading of fees1 app")


def fees2(req):
    return HttpResponse("heading of fees2 app")
