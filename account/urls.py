from django.urls import path
from . import views

urlpatterns = [
    # path('signup/', views.signup, name='signup'),
    path('signup/complete/', views.complete_signup, name='complete_signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('account/', views.account_view, name='account_view'),
    path('account/edit/', views.account_edit, name='account_edit'),
    path('otp/request/', views.request_otp, name='request_otp'),
    path('otp/verify/', views.verify_otp, name='verify_otp'),
    path('password-reset/', views.password_reset, name='password_reset'),
]