from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.conf import settings
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # читаем данные из CSV файла
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile) #первая строка= ключ словаря
        stations = list(reader) #собираем все словари в список
    page_number = request.GET.get('page', 1)  # 1 по умолчанию, если номер страницы не указан
    paginator = Paginator(stations, 10) #отображение 10 объектов на странице
    page = paginator.get_page(page_number)
    context = {
        'page': page
    }

    return render(request, 'stations/index.html', context)
