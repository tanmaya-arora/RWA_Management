# Generated by Django 4.2.1 on 2023-06-28 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0012_remove_member_res_address_remove_tenant_res_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('meeting_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
    ]
