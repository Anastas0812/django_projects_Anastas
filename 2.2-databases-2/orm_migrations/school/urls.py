from django.urls import path

from .views import students_list_view

urlpatterns = [
    path('', students_list_view, name='students'),
]
