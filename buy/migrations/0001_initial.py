# Generated by Django 5.0 on 2024-01-01 21:34

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('buyer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField()),
                ('payer_email', models.EmailField(max_length=250, null=True)),
                ('payer_document_type', models.CharField(blank=True, max_length=20)),
                ('payer_document_number', models.CharField(blank=True, max_length=50)),
                ('installaments', models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(36)])),
                ('issuer_id', models.CharField(blank=True, max_length=100)),
                ('payment_method_id', models.CharField(blank=True, max_length=20)),
                ('token', models.CharField(blank=True, max_length=250)),
                ('status', models.PositiveIntegerField(choices=[(1, 'CREADO'), (2, 'PENDIENTE'), (3, 'PAGADO'), (4, 'RECHAZADO')], default=1)),
                ('amount', models.PositiveIntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.buyer')),
            ],
            options={
                'db_table': 'buy',
            },
        ),
    ]
