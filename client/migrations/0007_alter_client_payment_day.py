# Generated by Django 5.0.1 on 2024-01-21 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_alter_client_payment_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='payment_day',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
