from django.urls import path
from .views import MeasurementListCreateAPIView, MeasurementRetrieveUpdateAPIView, MeasurementCreateAPIView


# все 5 запросов из requests.http выполнены
urlpatterns = [
    path('sensors/', MeasurementListCreateAPIView.as_view()), #создание и получение датчика
    path('sensors/<int:pk>/', MeasurementRetrieveUpdateAPIView.as_view()), #обновление датчика
    path('sensors/<int:pk>/', MeasurementListCreateAPIView.as_view()), #получение информации по датчику
    path('measurements/', MeasurementCreateAPIView.as_view()) #добавление измерения температуры
]