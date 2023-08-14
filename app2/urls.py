from django.urls import path
from app2.views import *
app_name='django_1'
urlpatterns = [
    path('document/',document,name="document"),
    path('facebook/',facebook,name="facebook"),
    path('table1/',table1,name="table1"),
    path('table2/',table2,name="table2"),
    path('amazon/',amazon,name="amazon"),
]