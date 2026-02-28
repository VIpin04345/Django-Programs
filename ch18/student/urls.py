from django.urls import path
from student.views import demo_form
urlpatterns=[
    path('',demo_form)
]