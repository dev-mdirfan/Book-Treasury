# Generated by Django 4.2.6 on 2023-12-12 15:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('about', models.TextField(blank=True, max_length=100)),
                ('college', models.CharField(max_length=200)),
                ('branch', models.CharField(max_length=200)),
                ('passing_year', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('is_best_seller', models.BooleanField(default=False)),
                ('join_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
