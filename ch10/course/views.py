from django.shortcuts import render


# Create your views here.
def learn_django(req):
    return render(req, "course/django.html",{'nm':'Django 5.x' , 'lang':'Go'})


def learn_python(req):
    return render(req, "course/python.html")
