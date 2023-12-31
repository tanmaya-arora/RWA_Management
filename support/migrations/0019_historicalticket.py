# Generated by Django 4.2.5 on 2023-10-09 03:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('support', '0018_alter_ticket_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalTicket',
            fields=[
                ('ticket_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('person_name', models.CharField(max_length=50)),
                ('person_email', models.EmailField(max_length=100)),
                ('phone_no', models.BigIntegerField()),
                ('date', models.DateTimeField(blank=True, editable=False)),
                ('message', models.TextField()),
                ('status', models.CharField(choices=[('closed', 'Closed'), ('pending', 'Pending'), ('opened', 'Opened'), ('reopened', 'Re opened')], max_length=28)),
                ('priority', models.CharField(choices=[('low', 'Low'), ('normal', 'Normal'), ('high', 'High')], default='Normal', max_length=12)),
                ('reply_message', models.TextField(null=True)),
                ('datetime_reply', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('replied_by', models.ForeignKey(blank=True, db_constraint=False, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='auth.group')),
            ],
            options={
                'verbose_name': 'historical ticket',
                'verbose_name_plural': 'historical tickets',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
