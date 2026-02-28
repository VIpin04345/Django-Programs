from django.urls import path
from student.views import register,success
urlpatterns=[
    path('',register,name='register'),
    path('success/',success,name='success')
]