from django.contrib import admin
from student.models import Profile
# Register your models here.

class ProfilAdmin(admin.ModelAdmin):
    list_display=('id','name' ,'email' ,'age' , 'city')
admin.site.register(Profile,ProfilAdmin)