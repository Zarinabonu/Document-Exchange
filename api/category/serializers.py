from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from category.models import Category, File, Files


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('category', )


class DocumentSerializer(ModelSerializer):
    class Meta:
        model = File
        fields = ()

    def create(self, validated_data):
        request = self.context['request']
        users = User.objects.get(id=1)
        f = File.objects.create(sender=users, name='test')
        name = request.data.get('name')
        files = request.data.getlist('file')
        print(files)
        for fil in files:
            print(fil)
            fi = Files.objects.create(files=f, file=fil)
            # fi.file.save(name='123', )
            fi.save()


        return f


