# Generated by Django 5.0.3 on 2024-03-30 13:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=20)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('description', models.TextField()),
                ('delivery_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cargo_deliveries', to='logistics.location')),
                ('pick_up_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cargo_pick_ups', to='logistics.location')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_number', models.CharField(max_length=6, unique=True)),
                ('carrying_capacity', models.IntegerField()),
                ('current_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logistics.location')),
            ],
        ),
    ]