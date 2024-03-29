# Generated by Django 5.0.1 on 2024-01-09 09:12

import django.db.models.deletion
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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default=None)),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_address', models.CharField(max_length=50)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(db_index=True, default=0)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(db_index=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EcomApp.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField(default=1)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='EcomApp.category')),
            ],
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EcomApp.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EcomApp.product')),
            ],
        ),
        migrations.CreateModel(
            name='OderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EcomApp.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EcomApp.product')),
            ],
            options={
                'unique_together': {('order', 'product')},
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EcomApp.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EcomApp.product')),
            ],
            options={
                'unique_together': {('product', 'customer')},
            },
        ),
    ]
