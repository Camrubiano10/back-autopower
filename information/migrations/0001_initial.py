# Generated by Django 5.0 on 2023-12-28 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('tipo_documento', models.CharField(max_length=50)),
                ('numero_doc', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.FloatField()),
                ('email', models.CharField(max_length=200)),
                ('tipo_vehiculo', models.CharField(max_length=200)),
                ('placa_vehiculo', models.CharField(max_length=10)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'information',
            },
        ),
    ]
