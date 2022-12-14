# Generated by Django 4.1.2 on 2022-10-13 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sukaldari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('photo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Platera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('price', models.FloatField()),
                ('photo', models.TextField()),
                ('sukaldari', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jatetxe.sukaldari')),
            ],
        ),
    ]
