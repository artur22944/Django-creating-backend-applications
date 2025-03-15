from rest_framework import generics

from measurement.models import Sensor, Measurement
from measurement.serializers import (
    SensorSerializer,
    MeasurementSerializer,
    SensorDetailSerializer,
)


class SensorView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDetailView(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementView(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
