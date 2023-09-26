# Generated by Django 4.2.1 on 2023-09-26 07:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('internal', '0003_alter_package_attributes_package_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductStock',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=250, verbose_name='Product Name')),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SaleHistory',
            fields=[
                ('date', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('Payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internal.payment')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internal.package_category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentHistory',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internal.payment')),
            ],
        ),
    ]
