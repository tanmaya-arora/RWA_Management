# Generated by Django 4.2.1 on 2023-06-28 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0011_society'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='res_address',
        ),
        migrations.RemoveField(
            model_name='tenant',
            name='res_address',
        ),
        migrations.AddField(
            model_name='member',
            name='res_area',
            field=models.ForeignKey(default='NA', on_delete=django.db.models.deletion.CASCADE, to='member.society'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='res_city',
            field=models.ForeignKey(default='NA', on_delete=django.db.models.deletion.CASCADE, to='member.city'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='res_country',
            field=models.ForeignKey(default='NA', on_delete=django.db.models.deletion.CASCADE, to='member.country'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='res_hno',
            field=models.IntegerField(default=9999999),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='res_state',
            field=models.ForeignKey(default='NA', on_delete=django.db.models.deletion.CASCADE, to='member.state'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tenant',
            name='res_area',
            field=models.ForeignKey(default='NA', on_delete=django.db.models.deletion.CASCADE, to='member.society'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tenant',
            name='res_city',
            field=models.ForeignKey(default='NA', on_delete=django.db.models.deletion.CASCADE, to='member.city'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tenant',
            name='res_country',
            field=models.ForeignKey(default='NA', on_delete=django.db.models.deletion.CASCADE, to='member.country'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tenant',
            name='res_hno',
            field=models.IntegerField(default=9999999),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tenant',
            name='res_state',
            field=models.ForeignKey(default='NA', on_delete=django.db.models.deletion.CASCADE, to='member.state'),
            preserve_default=False,
        ),
    ]
