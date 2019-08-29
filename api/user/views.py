from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from category.models import Category, File
from .serializers import User_Serializer
from django.contrib.auth.models import User
from user.models import Profile


class User_CreateAPIView(CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = User_Serializer
