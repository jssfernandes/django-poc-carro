# Generated by Django 4.0.2 on 2022-02-06 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fabricante', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=100)),
                ('ano_fabricacao', models.IntegerField()),
                ('pais_origem', models.CharField(max_length=100)),
                ('potencia_motor', models.IntegerField()),
                ('fabricante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fabricante.fabricante')),
            ],
        ),
    ]
