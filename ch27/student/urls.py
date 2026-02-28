from django.urls import path,register_converter
from student.views import home,profile
from student.converters import FourDigitYearConvertor
register_converter(FourDigitYearConvertor, 'yyyy')
urlpatterns = [
    path("", home, name="home"),
    # path('profile/<my_id>',profile,name='profile')
    # path('profile/<int:my_id>',profile,name='profile'),
    # path("profile/slug:title", profile, name="profile")
    # path("profile/str:<my_id>", profile, name="profile"),
    # path('profile/<str:my_class>/<int:my_id>',profile,name='profile')
    # path("profile/<str:my_class>/<int:my_id>", profile, name="profile"),
    path("profile/<yyyy:year>", profile, name="profile"),
]
