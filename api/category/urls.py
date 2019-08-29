from django.contrib import admin
from django.urls import path, include

from api.category import views

urlpatterns = [
    path('create/', views.Category_CreateAPIView.as_view(), name='api-category-create'),
    path('create/document/', views.Document_List.as_view(), name='api-document-create'),

]