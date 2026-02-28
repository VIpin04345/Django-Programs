from django.urls import path
from course.views import course1,course2
urlpatterns=[
    path('course1/',course1),
    path('course2/',course2),
]