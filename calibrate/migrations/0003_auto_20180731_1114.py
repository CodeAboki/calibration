# Generated by Django 2.0.7 on 2018-07-31 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calibrate', '0002_auto_20180731_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calibration',
            name='job_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='calibration',
            name='tyre_guage',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
