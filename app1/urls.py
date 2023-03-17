from app1.views import *
from django.urls import path
app_name='app1'
urlpatterns=[
    path('hari/',hari,name='hari'),
    path('parvathi/',parvathi,name='parvathi'),
]