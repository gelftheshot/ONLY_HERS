# Generated by Django 5.0.2 on 2024-03-27 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_orderitem_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='review',
        ),
    ]