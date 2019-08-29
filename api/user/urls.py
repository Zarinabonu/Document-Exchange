from django.contrib import admin
from django.urls import path, include

from api.user import views

urlpatterns = [
    path('create/', views.User_CreateAPIView.as_view(), name='api-user-create')
]