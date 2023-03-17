from app2.views import *
from django.urls import path
app_name='app2'
urlpatterns=[
    path('anil/',anil,name='anil'),
    path('nithish/',nithish,name='nithish'),
]