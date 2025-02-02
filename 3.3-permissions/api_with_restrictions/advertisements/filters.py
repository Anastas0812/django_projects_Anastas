from django_filters import rest_framework as filters

from .models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    creator = filters.NumberFilter(field_name='creator__id', lookup_expr='exact')
    status = filters.ChoiceFilter(field_name='status', choices=[
        ('OPEN', 'Открыто'),
        ('CLOSED', 'Закрыто'),
    ], lookup_expr='exact')
    created_at = filters.DateFromToRangeFilter(field_name='created_at', lookup_expr='range')

    class Meta:
        model = Advertisement
        fields = ['creator', 'created_at', 'status',]
