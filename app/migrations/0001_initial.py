# Generated by Django 5.1.3 on 2024-11-09 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Modelo', models.CharField(max_length=150)),
                ('Marca', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
            ],
        ),
    ]