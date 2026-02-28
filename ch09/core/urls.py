from django.urls import path
from core.views import about,home
urlpatterns=[
    path('',home , name='home'),
    path('about11/',about , name='about')
]