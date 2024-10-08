# Generated by Django 5.0.2 on 2024-03-30 07:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_remove_shipments_shipped_order_shipped'),
        ('userauths', '0004_alter_profile_profile_photo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SuperModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('color', models.CharField(choices=[('Very_light', 'Very light or pale'), ('Light', 'Light'), ('Medium', 'Medium'), ('Olive', 'Olive'), ('Tan', 'Tan'), ('Brown', 'Brown'), ('Dark', 'Dark'), ('Very_dark', 'Very dark or black')], max_length=50)),
                ('hair_type', models.CharField(choices=[('Straight', 'Straight hair'), ('Wavy', 'Wavy hair'), ('Curly', 'Curly hair'), ('Kinky', 'Kinky hair'), ('Coarse', 'Coarse hair'), ('Fine', 'Fine hair'), ('Thick', 'Thick hair'), ('Thin', 'Thin hair'), ('Frizzy', 'Frizzy hair')], max_length=50)),
                ('skin_type', models.CharField(choices=[('Dry', 'Dry skin'), ('Oily', 'Oily skin'), ('Normal', 'Normal skin'), ('Combination', 'Combination skin')], max_length=50)),
                ('instagram', models.CharField(max_length=100)),
                ('tiktok', models.CharField(max_length=100)),
                ('snapchat', models.CharField(max_length=100)),
                ('products', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.product')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='userauths.profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
