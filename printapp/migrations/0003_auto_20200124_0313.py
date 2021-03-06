# Generated by Django 3.0.2 on 2020-01-23 21:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printapp', '0002_auto_20200123_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='Date',
            field=models.DateField(default=datetime.datetime(2020, 1, 24, 3, 13, 21, 665756)),
        ),
        migrations.AlterField(
            model_name='order',
            name='Date',
            field=models.DateField(default=datetime.datetime(2020, 1, 24, 3, 13, 21, 659754)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='Date',
            field=models.DateField(default=datetime.datetime(2020, 1, 24, 3, 13, 21, 662757)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='paidIn',
            field=models.CharField(choices=[('Cash', 'Cash'), ('cheque', 'Cheque'), ('Online', 'Online')], default='Cash', max_length=10),
        ),
    ]
