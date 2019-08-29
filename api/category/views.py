from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView

from category.models import Category, File
from .serializers import CategorySerializer, DocumentSerializer, DocumentListSerializer


class Category_CreateAPIView(CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class Document_Create(CreateAPIView):
    queryset = File.objects.all()
    serializer_class = DocumentSerializer


class Document_List(ListAPIView):

    serializer_class = DocumentListSerializer

    def get_queryset(self):
        qs = File.objects.all()
        user = User.objects.get(id=self.request.user.id)
        qs = qs.filter(sender__profile__category=user.profile.category)
        return qs

          # u = User.objects.get(id=self.request.user.id)
          # c = u.profile.category
          # set = c.profile_set
          # if u==set:
          #     f = File.
          #
          # return set








