# Generated by Django 5.0.2 on 2024-03-20 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='Hot',
            field=models.BooleanField(default=False),
        ),
    ]