# Generated by Django 5.0.1 on 2024-01-26 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0009_client_date_start_alter_client_license_plate'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='date_end',
            field=models.CharField(default='26/02', max_length=5),
        ),
    ]
