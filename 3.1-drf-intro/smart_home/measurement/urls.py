from django.urls import path
from .views import SensorListCreateAPIView, SensorRetrieveUpdateAPIView, MeasurementCreateAPIView


# все 5 запросов из requests.http выполнены
urlpatterns = [
    path('sensors/', SensorListCreateAPIView.as_view()), #создание и получение датчика
    path('sensors/<int:pk>/', SensorRetrieveUpdateAPIView.as_view()), #обновление датчика
    path('measurements/', MeasurementCreateAPIView.as_view()) #добавление измерения температуры
]