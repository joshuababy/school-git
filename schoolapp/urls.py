from django.urls import path
from.views import *
urlpatterns = [
    path('',home,name='homepage'),
    path('abt/',about,name='about'),
    path('cnt/',contact,name='contact_us'),
    path('glry/',gallery,name='gallery'),
    path('carrier/',carriers,name='Carriers'),
    path('adm/',Admission,name='Admission'),
    path('std/',viewstudent,name='studentview'),
    path('log/',loginfn,name='login'),
]