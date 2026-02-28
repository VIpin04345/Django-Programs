from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello2(request):
    return HttpResponse("<h1> this is the first heading of app2 </h1>")


def parah2(request):
    return HttpResponse("<p> this is the first parah of app2</p>")
