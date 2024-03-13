# Generated by Django 5.0.3 on 2024-03-07 16:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift_type', models.CharField(choices=[('Day', 'Day Shift'), ('Night', 'Night Shift')], max_length=10)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('joining_date', models.DateTimeField(blank=True, null=True)),
                ('is_available', models.BooleanField(default=True)),
                ('shift_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.shift')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('resolution_end_date', models.DateTimeField(blank=True, null=True)),
                ('assigned_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.employee')),
            ],
        ),
    ]