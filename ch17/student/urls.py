from django.urls import path
from student.views import register,address,login
urlpatterns=[
    path('',register),
    path('ad/',address),
    path('lg/',login)
]