from django.forms import ModelForm
from.models import *
from django import Student
from.models import Teacher
class newstudent(ModelForm):
    class  Meta:
        model=Student
        fields='__all__'

class newteacher(ModelForm):
    class  Meta:
        model=Teacher
        fields='__all__'
