# Generated by Django 5.0.6 on 2024-07-06 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.ImageField(default='default_category_image.jpg', upload_to='category_images'),
        ),
    ]
