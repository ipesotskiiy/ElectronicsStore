# Generated by Django 4.0.1 on 2022-07-16 18:40

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255, verbose_name='Product type')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Product type',
                'verbose_name_plural': 'Product types',
            },
        ),
        migrations.CreateModel(
            name='MobilePhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Product name')),
                ('price', models.DecimalField(db_index=True, decimal_places=2, max_digits=12, validators=[django.core.validators.DecimalValidator(decimal_places=2, max_digits=11)], verbose_name='Price')),
                ('slug', models.SlugField(unique=True)),
                ('manufacturer_name', models.CharField(db_index=True, max_length=255, verbose_name='Manufacturer name')),
                ('discount', models.FloatField(blank=True, db_index=True, null=True, verbose_name='Discount')),
                ('photo', models.ImageField(upload_to='', verbose_name='Product photo')),
                ('description', models.TextField(max_length=255, verbose_name='Description')),
                ('color', models.CharField(max_length=255, verbose_name='Color')),
                ('count', models.PositiveIntegerField(verbose_name='Quantity in stock')),
                ('number_of_camera', models.IntegerField(validators=[django.core.validators.MaxValueValidator(limit_value=4, message='No more than four'), django.core.validators.MinValueValidator(limit_value=1, message='At least one')], verbose_name='Number of camera')),
                ('number_of_sim_cards', models.IntegerField(validators=[django.core.validators.MaxValueValidator(limit_value=3, message='No more than three'), django.core.validators.MinValueValidator(limit_value=1, message='At least one')], verbose_name='Number of SIM cards')),
                ('screen_refresh_rate_hertz', models.PositiveIntegerField(db_index=True, verbose_name='Screen refresh rate hertz')),
                ('screen_size', models.FloatField(db_index=True, verbose_name='Screen size')),
                ('screen_resolution', models.CharField(db_index=True, max_length=255, verbose_name='Screen resolution')),
                ('screen_matrix', models.CharField(db_index=True, max_length=255, verbose_name='Screen matrix')),
                ('cpu_name', models.CharField(db_index=True, max_length=255, verbose_name='CPU')),
                ('ram_in_gigabytes', models.IntegerField(db_index=True, validators=[django.core.validators.MaxValueValidator(limit_value=256, message='No more than two hundred and fifty six'), django.core.validators.MinValueValidator(limit_value=1, message='At least one')], verbose_name='RAM in gigabytes')),
                ('weight', models.FloatField(verbose_name='Weight in kilograms')),
                ('operating_system', models.CharField(db_index=True, max_length=255, verbose_name='Operating system')),
                ('battery_capacity_in_milliamps', models.IntegerField(verbose_name='Battery capacity in milliamps')),
                ('built_in_memory_in_gigabytes', models.IntegerField(verbose_name='Built-in memory in gigabytes')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.producttype')),
            ],
            options={
                'verbose_name': 'Mobile Phone',
                'verbose_name_plural': 'Mobile Phones',
            },
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Product name')),
                ('price', models.DecimalField(db_index=True, decimal_places=2, max_digits=12, validators=[django.core.validators.DecimalValidator(decimal_places=2, max_digits=11)], verbose_name='Price')),
                ('slug', models.SlugField(unique=True)),
                ('manufacturer_name', models.CharField(db_index=True, max_length=255, verbose_name='Manufacturer name')),
                ('discount', models.FloatField(blank=True, db_index=True, null=True, verbose_name='Discount')),
                ('photo', models.ImageField(upload_to='', verbose_name='Product photo')),
                ('description', models.TextField(max_length=255, verbose_name='Description')),
                ('color', models.CharField(max_length=255, verbose_name='Color')),
                ('count', models.PositiveIntegerField(verbose_name='Quantity in stock')),
                ('number_of_ram_slots', models.IntegerField(validators=[django.core.validators.MaxValueValidator(limit_value=3, message='No more than three'), django.core.validators.MinValueValidator(limit_value=1, message='At least one')], verbose_name='Number of RAM slots')),
                ('video_card_type', models.CharField(db_index=True, max_length=255, verbose_name='Video card type')),
                ('video_processor', models.CharField(db_index=True, max_length=255, verbose_name='Video processor')),
                ('memory_storage_type', models.CharField(max_length=255, verbose_name='Memory storage type')),
                ('screen_refresh_rate_hertz', models.PositiveIntegerField(db_index=True, verbose_name='Screen refresh rate hertz')),
                ('screen_size', models.FloatField(db_index=True, verbose_name='Screen size')),
                ('screen_resolution', models.CharField(db_index=True, max_length=255, verbose_name='Screen resolution')),
                ('screen_matrix', models.CharField(db_index=True, max_length=255, verbose_name='Screen matrix')),
                ('cpu_name', models.CharField(db_index=True, max_length=255, verbose_name='CPU')),
                ('ram_in_gigabytes', models.IntegerField(db_index=True, validators=[django.core.validators.MaxValueValidator(limit_value=256, message='No more than two hundred and fifty six'), django.core.validators.MinValueValidator(limit_value=1, message='At least one')], verbose_name='RAM in gigabytes')),
                ('weight', models.FloatField(verbose_name='Weight in kilograms')),
                ('operating_system', models.CharField(db_index=True, max_length=255, verbose_name='Operating system')),
                ('battery_capacity_in_milliamps', models.IntegerField(verbose_name='Battery capacity in milliamps')),
                ('built_in_memory_in_gigabytes', models.IntegerField(verbose_name='Built-in memory in gigabytes')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.producttype')),
            ],
            options={
                'verbose_name': 'Laptop',
                'verbose_name_plural': 'Laptops',
            },
        ),
        migrations.CreateModel(
            name='Freezer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Product name')),
                ('price', models.DecimalField(db_index=True, decimal_places=2, max_digits=12, validators=[django.core.validators.DecimalValidator(decimal_places=2, max_digits=11)], verbose_name='Price')),
                ('slug', models.SlugField(unique=True)),
                ('manufacturer_name', models.CharField(db_index=True, max_length=255, verbose_name='Manufacturer name')),
                ('discount', models.FloatField(blank=True, db_index=True, null=True, verbose_name='Discount')),
                ('photo', models.ImageField(upload_to='', verbose_name='Product photo')),
                ('description', models.TextField(max_length=255, verbose_name='Description')),
                ('color', models.CharField(max_length=255, verbose_name='Color')),
                ('count', models.PositiveIntegerField(verbose_name='Quantity in stock')),
                ('total_usable_volume_in_liters', models.FloatField(db_index=True, verbose_name='Total usable volume in liters')),
                ('minimum_temperature_in_degrees_Celsius', models.FloatField(verbose_name='Minimum temperature in degrees Celsius')),
                ('noise_level_in_decibels', models.FloatField(verbose_name='Noise level in decibels')),
                ('total_number_of_boxes', models.IntegerField(verbose_name='Total number of boxes')),
                ('number_of_drawers', models.IntegerField(verbose_name='Number of drawers')),
                ('number_of_drawers_with_doors', models.IntegerField(verbose_name='Number of drawers with doors')),
                ('power_consumption_in_watts', models.FloatField(verbose_name='Power consumption in watts')),
                ('refrigerant', models.CharField(max_length=255, verbose_name='Refrigerant')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.producttype')),
            ],
            options={
                'verbose_name': 'Freezer',
                'verbose_name_plural': 'Freezers',
            },
        ),
    ]
