# Generated by Django 5.0.1 on 2024-01-21 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_alter_client_payment_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='payment_day',
        ),
    ]