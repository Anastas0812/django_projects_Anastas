from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer



# получение + создание датчиков (GET, POST запросы)
class SensorListCreateAPIView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

#обновление датчика (PATCH)
class SensorRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

# добавление измерения (POST)
class MeasurementCreateAPIView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


