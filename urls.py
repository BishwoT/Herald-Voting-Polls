# myproject/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='home'),  
    path('signup/', views.signup, name='signup'),  
]



# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Add this line to map the root URL to the home view
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('verify-otp/<int:user_id>/', views.verify_otp, name='verify_otp'),
]
