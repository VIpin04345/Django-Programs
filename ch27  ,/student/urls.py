from django.urls import path
from student.views import home, candidate_details

urlpatterns = [
    path("", home, name="home"),
    path("candidate/<int:pk>", candidate_details, name="candi"),
]
