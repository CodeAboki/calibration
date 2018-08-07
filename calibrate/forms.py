from django import forms
from calibrate.models import Calibration


class CalibrationForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'First Name'
        }
    ))

    last_name = forms.CharField(widget = forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Last Name'
        }
    ))


    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(
        attrs={
            'class':'form-control',
            'placeholder':'Select'
        }
    ))

    STATE_CHOICE = (
        ('ABIA', 'ABIA'),
        ('ADAMAWA', 'ADAMAWA'),
        ('AKWA IBOM', 'AKWA IBOM'),
        ('KANO', 'KANO')
    )

    state= forms.ChoiceField(choices=STATE_CHOICE, widget=forms.Select( 
        attrs = {
            'class':'form-control'
        }
    ))

    phone = forms.IntegerField(widget=forms.NumberInput( 
        attrs={
            'class':'form-control',
            'placeholder':'Phone Number'
        }
    ))

    email = forms.EmailField(widget =forms.EmailInput( 
        attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        }
    ))

    tyre_make = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Tyre Make'
        }
    ))

    tyre_guage = forms.IntegerField(widget = forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'Tyre Guage'
        }
    ))
 

    VALVE_POSITION_CHOICES = (
        ('OPEN', 'OPEN'),
        ('CLOSE', 'CLOSE'),
        ('NONE', 'NONE')
    )

    valve_position = forms.ChoiceField(choices=VALVE_POSITION_CHOICES, widget=forms.Select(
        attrs={
            'class':'form-control',
            'placeholder':'Valve Position'
        }
    ))

    job_number = forms.IntegerField(widget = forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'Job Number'
        }
    ))



    TANK_POSITION_CHOICES = (
        ('BALLON', 'BALLON'),
        ('SPRING', 'SPRING')
    )

    tank_position = forms.ChoiceField(choices=TANK_POSITION_CHOICES , widget = forms.Select(
        attrs={
            'class':'form-control',
            'placeholder':'Tank Position'
        }
    ))

    registration_number = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Registration Number'
        }
    ))

    transporter = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Transporter'
        }
    ))

    chasis_number = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'Chasis Number'
        }
    ))
    
    date_issued = forms.CharField(widget=forms.DateInput(
        attrs={
            'class':'form-control',
            'placeholder':'yyyy-mm-dd'
        }
    ))

    date_expired = forms.CharField(widget=forms.DateInput(
        attrs={
            'class':'form-control',
            'placeholder':'yyyy-mm-dd'
        }
    ))

    certificate_number = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'Certificate Number'
        }
    ))

    capacity = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'Capacity'
        }
    ))

    document = forms.FileField(widget=forms.FileInput(
        attrs={
            'class':'form-control'
        }
    ))

      

    class Meta:
        model = Calibration
        fields = ('first_name', 'last_name','gender','state','phone','email',
                'tyre_make','tyre_guage','valve_position','job_number','tank_position',
                'registration_number','transporter','chasis_number','date_issued','date_expired',
                'certificate_number','capacity','document')
