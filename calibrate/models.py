from django.db import models
from django.urls import reverse 
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Calibration(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    
    GENDER_CHOICES = (
        ('M', 'MALE'),
        ('F', 'FEMALE')
    )
    gender = models.CharField(max_length = 1, choices =GENDER_CHOICES)
    
    STATE_CHOICE = (
        ('ABIA', 'ABIA'),
        ('ADAMAWA', 'ADAMAWA'),
        ('AKWA IBOM', 'AKWA IBOM'),
        ('KANO', 'KANO')
    )
    state = models.CharField(max_length = 20, choices = STATE_CHOICE)

    phone = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=200)
    tyre_make = models.CharField(max_length=200)
    tyre_guage = models.IntegerField(blank=True, null=True)

    VALVE_POSITION_CHOICES = (
        ('OPEN', 'OPEN'),
        ('CLOSE', 'CLOSE'),
        ('NONE', 'NONE')
    )
    valve_position = models.CharField(max_length =20, choices = VALVE_POSITION_CHOICES)
    
    job_number = models.IntegerField(blank=True, null=True)

    TANK_POSITION_CHOICES = (
        ('BALLON', 'BALLON'),
        ('SPRING', 'SPRING')
    )
    tank_position = models.CharField(max_length=200, choices=TANK_POSITION_CHOICES)
    registration_number= models.CharField(max_length=200)
    transporter = models.CharField(max_length=200)
    chasis_number = models.CharField(max_length=200)
    date_issued = models.DateField(blank=True, null=True)
    date_expired = models.DateField(blank=True, null=True)
    certificate_number = models.IntegerField(default=0)
    capacity = models.IntegerField(default=0) 
    document = models.FileField(upload_to='documents')
    
    def __str__(self):
       return self.first_name

    def get_absolute_url(self):
        return reverse('calibrate:calibration_edit', kwargs={'pk': self.pk})

    def status(self):
        today = datetime.date.today()
        difference = self.date_expired - today
        if difference.days <=0:
            status_code = "Expired"
        else:
            status_code = "Active"
        return status_code

 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type_choices = (
        ('regular_admin', 'Admin'),
        ('super_admin', 'Super Admin')
    )
    userType = models.CharField(max_length = 50, choices = user_type_choices, blank=True, null=True)

    def __str__(self):
        return self.user.profile.userType


   

    
@receiver(post_save, sender=User)
def user_is_created(sender, instance, created, **kwargs):
    print(created)
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()