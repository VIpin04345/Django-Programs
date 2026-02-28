from django.urls import path
from school.views import stu_register,tea_register,success
urlpatterns=[
    path('stu/',stu_register),
    path('tea/',tea_register),
    path('success/',success)
]