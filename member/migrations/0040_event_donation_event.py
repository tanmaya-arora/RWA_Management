# Generated by Django 4.2.1 on 2023-08-29 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0039_donation_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='donation',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.event'),
            preserve_default=False,
        ),
    ]