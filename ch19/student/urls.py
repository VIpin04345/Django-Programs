from django.urls import path
from student.views import register,success
urlpatterns=[
    path('',register),
    path('success/',success)
]