# Generated by Django 2.2.4 on 2019-08-29 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20190829_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='files',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filees', to='category.File'),
        ),
    ]