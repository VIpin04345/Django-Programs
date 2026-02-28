from django.urls import path
from fees.views import fees1,fees2

urlpatterns = [
    path("fees1/", fees1),
    path("fees2/", fees2),
]
