# Generated by Django 5.0.2 on 2024-04-05 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_supermodel_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supermodel',
            name='name',
        ),
    ]