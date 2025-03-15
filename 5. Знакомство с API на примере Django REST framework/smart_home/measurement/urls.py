from django.urls import path

from measurement.views import SensorView, MeasurementView, SensorDetailView

urlpatterns = [
    path("sensors/", SensorView.as_view(), name="sensor_list"),
    path("measurements/", MeasurementView.as_view(), name="measurement_list"),
    path("sensors/<pk>/", SensorDetailView.as_view(), name="sensor_detail"),
]
