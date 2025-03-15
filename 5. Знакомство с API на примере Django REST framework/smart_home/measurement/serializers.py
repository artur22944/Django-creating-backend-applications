from rest_framework import serializers
from measurement.models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ["id", "name", "description"]


class MeasurementFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ["id", "sensor", "temperature", "created_at"]


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta(MeasurementFullSerializer.Meta):
        fields = ["temperature", "created_at"]


class SensorDetailSerializer(serializers.ModelSerializer):
    Measurement = MeasurementSerializer(many=True, read_only=True)

    class Meta(SensorSerializer.Meta):
        fields = SensorSerializer.Meta.fields + ["Measurement"]
