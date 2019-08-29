from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from category.models import Category


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)


@receiver(post_save, sender=User)
def create_doctor_user(sender, instance, created, **kwargs):
    if created:
        p = Profile.objects.create(user=instance)
