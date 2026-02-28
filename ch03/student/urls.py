from django.urls import path
from student.views import var, hello,operation,html
urlpatterns=[
    path('hello/',hello),
    path('var/',var),
    path('operation/',operation),
    path('html/',html)
]