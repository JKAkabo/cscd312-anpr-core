# Generated by Django 3.0.7 on 2020-06-12 08:29

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processedimage',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
    ]
