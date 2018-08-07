from django.urls import path

from . import views

app_name = 'calibrate'

urlpatterns = [
  path('', views.CalibrationList.as_view(), name='calibration_list'),
  path('new', views.CalibrationCreate.as_view(), name='calibration_new'),
  path('edit/<int:pk>', views.CalibrationUpdate.as_view(), name='calibration_edit'),
  path('delete/<int:pk>', views.CalibrationDelete.as_view(), name='calibration_delete'),
  ]