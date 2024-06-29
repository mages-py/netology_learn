# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import generics
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetalilSerializer


class SensorView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDetailView(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.prefetch_related('measurements').all()
    serializer_class = SensorDetalilSerializer


class MeasurementsAddView(generics.ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def perform_create(self, serializer):
        sensor = generics.get_object_or_404(
            Sensor, id=self.request.data.get('sensor'))
        return serializer.save(sensor=sensor)
