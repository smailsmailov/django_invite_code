from django.contrib import admin
from django.urls import path , include
from .views import * 


urlpatterns = [
    path("login/" , login_page , name = "login"),
    path("" , home_page , name = "home"),    
    path("profile/" , profile_page , name = "profile"),   
    # path("accounts/", include("django.contrib.auth.urls")),
]
# API

urlpatterns += [
    path('get_code/' , GetCodeAuth , name = "get_code"),
    path('get_all_users/' , GetAllUsersInvites , name='get_all_users')
]
