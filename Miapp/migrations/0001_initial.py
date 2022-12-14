# Generated by Django 4.1.2 on 2022-10-28 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Celulares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo_celular', models.CharField(max_length=50)),
                ('stock_celular', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_hardware', models.CharField(max_length=50)),
                ('marca_hardware', models.CharField(max_length=50)),
                ('stock_hardware', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Insumos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_insumo', models.CharField(max_length=50)),
                ('marca_insumo', models.CharField(max_length=50)),
                ('stock_insumo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_software', models.CharField(max_length=50)),
                ('marca_software', models.CharField(max_length=50)),
                ('stock_software', models.IntegerField()),
            ],
        ),
    ]
