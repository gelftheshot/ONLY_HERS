# Generated by Django 5.0.2 on 2024-03-29 09:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_remove_wishlist_product_wishlistproduct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipments',
            name='cart',
        ),
        migrations.AddField(
            model_name='shipments',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.order'),
        ),
        migrations.AddField(
            model_name='shipments',
            name='shipped',
            field=models.BooleanField(default=False),
        ),
    ]
