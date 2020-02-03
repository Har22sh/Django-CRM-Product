# Generated by Django 3.0.1 on 2020-01-29 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('printapp', '0011_auto_20200126_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='attachments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(upload_to='')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='printapp.Order')),
            ],
        ),
    ]
