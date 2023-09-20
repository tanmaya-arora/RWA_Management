# Generated by Django 4.2.5 on 2023-09-20 07:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('member', '0054_remove_member_res_area_remove_member_res_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('tenant_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('', ''), ('M', 'male'), ('F', 'female')], default='', max_length=12)),
                ('phone_no', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('res_hno', models.IntegerField()),
                ('marital_status', models.CharField(default='Single', max_length=50)),
                ('is_verified', models.BooleanField(default=False)),
                ('otp', models.CharField(max_length=10)),
                ('res_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.society')),
                ('res_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.city')),
                ('res_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.country')),
                ('res_state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.state')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='tenant', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('member_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('', ''), ('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')], default='', max_length=12)),
                ('phone_no', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('res_hno', models.SmallIntegerField()),
                ('is_verified', models.BooleanField(default=False)),
                ('otp', models.CharField(max_length=10)),
                ('res_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.society')),
                ('res_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.city')),
                ('res_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.country')),
                ('res_state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.state')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='member', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
