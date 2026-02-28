from django.urls import path
from app1.views import hello1, yes1
urlpatterns=[
    path('',hello1),
    path('yes1/',yes1)
]