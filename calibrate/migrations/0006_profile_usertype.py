# Generated by Django 2.0.7 on 2018-08-25 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calibrate', '0005_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='userType',
            field=models.CharField(blank=True, choices=[('0', 'Admin'), ('1', 'Super Admin')], max_length=1, null=True),
        ),
    ]
