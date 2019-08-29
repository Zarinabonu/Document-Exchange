from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView

from category.models import Category, File
from .serializers import CategorySerializer, DocumentSerializer


class Category_CreateAPIView(CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class Document_List(CreateAPIView):
    queryset = File.objects.all()
    serializer_class = DocumentSerializer







