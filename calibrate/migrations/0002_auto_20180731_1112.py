# Generated by Django 2.0.7 on 2018-07-31 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calibrate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calibration',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
