from django.shortcuts import render
from student.forms import Registration

# Create your views here.
def register(req):
    # form=Registration(label_suffix=':::')

    # form = Registration(label_suffix="=")
    # form = Registration(auto_id=True)
    # form = Registration(auto_id=False)
    # form = Registration(auto_id='shubh_%s')

    # form = Registration(initial={'name':'shubham','email':'xyz@gmail.com','age':'xx','city':'xyz'})
    # form = Registration(initial=True)

    form = Registration(field_order=['email','city'])

    return render(req, "student/register.html", {"forms": form})
