# myproject/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='home'),  
    path('signup/', views.signup, name='signup'),  
]
