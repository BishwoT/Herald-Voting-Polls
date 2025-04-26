
from django.urls import path
from myproject import views

urlpatterns = [
    path('', views.signup, name='signup'),  # Start with signup page
    path('verify_otp/<int:user_id>/', views.verify_otp, name='verify_otp'),  # OTP verification page
    path('login/', views.login_view, name='login'),  # Login page
    path('home/', views.home, name='home'),  # Home page after login
    path('logout/', views.logout_view, name='logout'),  # Logout view
]


 
