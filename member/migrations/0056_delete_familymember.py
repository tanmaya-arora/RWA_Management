# Generated by Django 4.2.1 on 2023-09-20 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0055_delete_member_delete_tenant'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FamilyMember',
        ),
    ]
