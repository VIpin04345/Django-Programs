from django.shortcuts import render


# Create your views here.
def about(req):
    return render(req, "core/about.html")


def home(req):
    return render(req, "core/home.html")
