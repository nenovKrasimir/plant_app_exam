# Generated by Django 4.2.2 on 2023-06-16 05:21

import django.core.validators
from django.db import migrations, models
import plant_app_exam_2023.myplantapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_type', models.CharField(max_length=14)),
                ('name', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, unique=True, validators=[django.core.validators.MinValueValidator(2)])),
                ('first_name', models.CharField(max_length=30, validators=[
                    plant_app_exam_2023.myplantapp.models.validate_capitalized_name])),
                ('last_name', models.CharField(max_length=30, validators=[
                    plant_app_exam_2023.myplantapp.models.validate_capitalized_name])),
                ('profile_picture', models.URLField(blank=True)),
            ],
        ),
    ]
