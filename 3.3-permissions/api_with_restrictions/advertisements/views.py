from rest_framework import permissions, status
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .filters import AdvertisementFilter
from .models import Advertisement
from .serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AdvertisementFilter

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def create(self, request, *args, **kwargs):
        user = request.user
        open_ads_count = Advertisement.objects.filter(creator=user, status='OPEN').count()
        if open_ads_count >= 10:
            return Response(
                {"detail": "Максимальное кол-во объявлений 10 шт. Вы не можете создать новое объявление."},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().create(request, *args, **kwargs)

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action == "create":
            return [IsAuthenticated()] # Только авторизованные пользователи могут создавать
        elif self.action in ['update', 'partial_update', 'destroy']:
            advertisement = self.kwargs.get('id')
            try:
                advertisement = self.get_queryset().get(id=advertisement)
            except Advertisement.DoesNotExist:
                return []
            if advertisement.creator != self.request.user:
                return []  # Только автор может обновлять или удалять
        return super().get_permissions()

    def update(self, request, *args, **kwargs):
        advertisement = self.get_object()
        if advertisement.creator != request.user:
            return Response(
                {"detail": "У вас нет прав на редактирование этого контента."},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        advertisement = self.get_object()
        if advertisement.creator != request.user:
            return Response(
                {"detail": "У вас нет прав на удаление этого контента."},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().destroy(request, *args, **kwargs)
