# Generated by Django 4.2.1 on 2023-07-27 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0021_alter_member_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='res_area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='member.society'),
        ),
        migrations.AlterField(
            model_name='member',
            name='res_city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='member.city'),
        ),
        migrations.AlterField(
            model_name='member',
            name='res_country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='member.country'),
        ),
        migrations.AlterField(
            model_name='member',
            name='res_state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='member.state'),
        ),
    ]
