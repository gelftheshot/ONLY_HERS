# Generated by Django 5.0.2 on 2024-03-27 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0003_profile_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(default='default.jpg', upload_to='profile_photos/'),
        ),
    ]
