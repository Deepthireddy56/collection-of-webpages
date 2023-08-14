from django.urls import path
from app3.views import *
app_name='django_2'
urlpatterns = [
    path('table3/',table3,name="table3"),
    path('table4/',table4,name="table4"),
    path('table5/',table5,name="table5"),
    path('table6/',table6,name="table6"),
    path('table7/',table7,name="table7"),
    
]