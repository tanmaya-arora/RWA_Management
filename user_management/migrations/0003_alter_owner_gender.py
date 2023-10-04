# Generated by Django 4.2.5 on 2023-10-03 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0002_alter_familymember_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='gender',
            field=models.CharField(choices=[('', ''), ('Male', 'Male'), ('Female', 'Female'), ('other', 'Other')], default='', max_length=12),
        ),
    ]