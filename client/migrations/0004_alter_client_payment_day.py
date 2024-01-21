# Generated by Django 5.0.1 on 2024-01-21 21:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_alter_client_payment_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='payment_day',
            field=models.DateField(validators=[django.core.validators.MaxValueValidator(31)]),
        ),
    ]
