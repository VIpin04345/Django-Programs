from django.shortcuts import render
from student.forms import Registration,Address,Login
# Create your views here.
def register(req):
    fm=Registration()
    return render(req,'student/registration.html',{'form':fm})


def address(req):
    fm = Address()
    return render(req, "student/address.html", {"form": fm})


def login(req):
    fm = Login()
    return render(req, "student/login.html", {"form": fm})
