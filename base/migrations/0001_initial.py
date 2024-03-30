# Generated by Django 5.0.2 on 2024-03-20 12:17

import base.models
import django.db.models.deletion
import shortuuid.django_fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cat_id', shortuuid.django_fields.ShortUUIDField(alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', editable=False, length=15, max_length=20, prefix='cat', primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Catagories',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(null=True, upload_to=base.models.get_product_details_upload_path)),
                ('image2', models.ImageField(null=True, upload_to=base.models.get_product_details_upload_path)),
                ('image3', models.ImageField(null=True, upload_to=base.models.get_product_details_upload_path)),
                ('image4', models.ImageField(null=True, upload_to=base.models.get_product_details_upload_path)),
                ('image5', models.ImageField(null=True, upload_to=base.models.get_product_details_upload_path)),
                ('image6', models.ImageField(null=True, upload_to=base.models.get_product_details_upload_path)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('blog_id', shortuuid.django_fields.ShortUUIDField(alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', editable=False, length=15, max_length=20, prefix='blog', primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to=base.models.get_blog_upload_path)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pro_id', shortuuid.django_fields.ShortUUIDField(alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', editable=False, length=15, max_length=20, prefix='pro', primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('display_image', models.ImageField(upload_to=base.models.get_product_upload_path)),
                ('new_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('old_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('percentage_discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('label', models.CharField(max_length=30)),
                ('in_stock', models.BooleanField(default=True)),
                ('Tranding', models.BooleanField(default=False)),
                ('Hot', models.BooleanField(default=False)),
                ('Category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.category')),
                ('infulancer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('deatail_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.productimage')),
            ],
        ),
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('pack_id', shortuuid.django_fields.ShortUUIDField(alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', editable=False, length=15, max_length=20, prefix='pack', primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to=base.models.get_package_upload_path)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('products', models.ManyToManyField(null=True, related_name='packages', to='base.product')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('zip_code', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('zip_code', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.product')),
            ],
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.product')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(choices=[(1, '★☆☆☆☆'), (2, '★★☆☆☆'), (3, '★★★☆☆'), (4, '★★★★☆'), (5, '★★★★★')], default=5)),
                ('review', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rated_products', to='base.review'),
        ),
        migrations.CreateModel(
            name='Shipments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('zip_code', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.cart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to=base.models.get_product_upload_path)),
                ('name', models.CharField(max_length=30)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.category')),
            ],
            options={
                'verbose_name': 'Sub Category',
                'verbose_name_plural': 'Sub Catagories',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='sub_Category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.subcategory'),
        ),
        migrations.AddField(
            model_name='category',
            name='sub_category',
            field=models.ManyToManyField(blank=True, related_name='categories', to='base.subcategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(blank=True, to='base.tag'),
        ),
        migrations.CreateModel(
            name='wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
