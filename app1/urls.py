from django.urls import path
from app1.views import *
app_name='django'
urlpatterns = [
    path('animation1/',animation1,name="animation1"),
    path('animation2/',animation2,name="animation2"),
    path('application/',application,name="application"),
    path('card/',card,name="card"),
    path('testing/',testing,name="testing"),
]