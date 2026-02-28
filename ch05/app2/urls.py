from django.urls import path
from app2.views import hello2, yes2
urlpatterns=[
    path('hello2/',hello2),
    path('yes2/',yes2),
]