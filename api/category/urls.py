from django.contrib import admin
from django.urls import path, include

from api.category import views

urlpatterns = [
    path('create/', views.Category_CreateAPIView.as_view(), name='api-category-create'),
    path('create/document/', views.Document_Create.as_view(), name='api-document-create'),
    path('document/list', views.Document_List.as_view(), name='api-document-list'),

]