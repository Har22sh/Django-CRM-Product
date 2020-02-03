# Generated by Django 2.2.4 on 2020-01-26 05:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Msupplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Company', models.CharField(max_length=30)),
                ('Mobile', models.CharField(max_length=12)),
                ('Address', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(default=datetime.datetime(2020, 1, 26, 10, 51, 42, 790932))),
                ('paidBy', models.CharField(choices=[('Cash', 'Cash'), ('cheque', 'Cheque'), ('Online', 'Online')], default='Cash', max_length=10)),
                ('Amount', models.IntegerField(default=0)),
                ('Comment', models.TextField(blank=True)),
                ('Msupplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='material.Msupplier')),
            ],
        ),
        migrations.CreateModel(
            name='MOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mname', models.CharField(max_length=30)),
                ('Date', models.DateField(default=datetime.datetime(2020, 1, 26, 10, 51, 42, 790932))),
                ('Size', models.CharField(blank=True, max_length=30)),
                ('gsm', models.IntegerField(blank=True)),
                ('Quantity', models.IntegerField()),
                ('Amount', models.IntegerField()),
                ('Comment', models.TextField(blank=True)),
                ('Msupplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='material.Msupplier')),
            ],
        ),
    ]
