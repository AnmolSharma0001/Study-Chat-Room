from django.urls import path
from django.http import HttpResponse
from . import views


urlpatterns = [
    path("", views.home, name='home'),
    path("room/<str:pk>/", views.room, name='room'),
    path("profile/<str:pk>/", views.userProfile, name='user-profile'),
    path("create-room/", views.createRoom, name='create-room'),
    path("update-room/<str:pk>/", views.updateRoom, name='update-room'),
    path("delete-room/<str:pk>/", views.deleteRoom, name='delete-room'),
    path("login/", views.loginPage, name='login'),
    path("logout/", views.logoutUser, name='logout'),
    path("register/", views.registerUser, name='register'),
    path("update-user/", views.updateUser, name='update-user'),
    path("delete-message/<str:pk>/", views.deleteMessage, name='delete-message'),
    path("topics/", views.topicPage, name='topics'),
    path("activity/", views.activityPage, name='activity'),    
]
