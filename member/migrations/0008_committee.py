# Generated by Django 4.2.1 on 2023-06-27 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0007_broadcast_alter_chat_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Committee',
            fields=[
                ('committee_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('position', models.CharField(max_length=50)),
            ],
        ),
    ]
