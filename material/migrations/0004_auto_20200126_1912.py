# Generated by Django 2.2.4 on 2020-01-26 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0003_auto_20200126_1911'),
    ]

    operations = [
        migrations.RenameField(
            model_name='morder',
            old_name='MName',
            new_name='OrderName',
        ),
        migrations.RenameField(
            model_name='morder',
            old_name='MsupplierName',
            new_name='supplierName',
        ),
    ]
