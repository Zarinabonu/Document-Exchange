from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category


class File(models.Model):
    sender = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    name = models.TextField(null=True)


class Files(models.Model):
    files = models.ForeignKey('File', on_delete=models.CASCADE, related_name='filees')
    file = models.FileField(upload_to='file/')
# Create your models here.
