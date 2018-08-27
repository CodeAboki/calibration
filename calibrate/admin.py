from django.contrib import admin
from calibrate.models import Calibration, Profile



class CalibrationAdmin(admin.ModelAdmin):
      GRAPPELLI_ADMIN_TITLE = 'Retail Calibration'
      list_display = ['transporter', 'registration_number', 'date_issued', 'date_expired', 'chasis_number',
      'certificate_number', 'capacity', 'document']
      search_fields = ['transporter', 'registration_number', 'date_issued', 'date_expired', 'chasis_number',
      'certificate_number', 'capacity', 'document']

admin.site.register(Calibration, CalibrationAdmin)
admin.site.register(Profile)