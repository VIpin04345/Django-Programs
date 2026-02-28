from django.urls import path
from student.views import register,login
urlpatterns=[
    path('',register),
    path('lg/',login)
]