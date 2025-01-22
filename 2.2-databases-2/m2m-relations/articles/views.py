from django.shortcuts import render

from .models import Article


def articles_list_view(request):
    template = 'articles/news.html'
    context = {}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'
    # Получаем все статьи и сортируем их по дате публикации
    articles = Article.objects.all().order_by(ordering)
    context = {
        'articles': articles,
    }

    return render(request, template, context)
