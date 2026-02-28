from django.urls import path
from student.views import data
urlpatterns=[
    path('',data)
]