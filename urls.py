from django.urls import path
from . import signup, login

urlpatterns = [
    path('C:\Users\PC\Desktop\OnlineVotingPoll\votingpoll\accounts', signup.signup, name='signup'),  
    path('C:\Users\PC\Desktop\OnlineVotingPoll\votingpoll\accounts', login.user_login, name='login'),  
]
