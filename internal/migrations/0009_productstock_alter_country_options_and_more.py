# Generated by Django 4.2.1 on 2024-01-03 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0008_payment_branch_name_payment_payment_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductStock',
            fields=[
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='internal.package_category')),
                ('quantity', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'Country', 'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterModelOptions(
            name='package_attributes',
            options={'verbose_name': 'Package Attribute', 'verbose_name_plural': 'Package Attributes'},
        ),
        migrations.AlterModelOptions(
            name='package_category',
            options={'verbose_name': 'Package Category', 'verbose_name_plural': 'Package Categories'},
        ),
        migrations.AlterModelOptions(
            name='society',
            options={'verbose_name': 'Society', 'verbose_name_plural': 'Societies'},
        ),
        migrations.RenameField(
            model_name='order',
            old_name='Payment',
            new_name='payment',
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(choices=[('online', 'Online'), ('offline', 'Offline')], max_length=50),
        ),
    ]
