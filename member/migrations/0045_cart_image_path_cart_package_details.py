# Generated by Django 4.2.1 on 2023-09-11 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0044_package_category_image_path_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='image_path',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='package_details',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
