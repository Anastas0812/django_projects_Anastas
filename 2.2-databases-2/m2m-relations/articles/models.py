from django.db import models
from django.core.exceptions import ValidationError


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField(Tag, through='Scope')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change:  # Если это новая запись
            print(f'Новая статья добавлена с ID: {obj.id}')



    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scope(models.Model):
    article = models.ForeignKey('Article', related_name='scopes', on_delete=models.CASCADE, null=True)
    tag = models.ForeignKey('Tag', related_name='scopes', on_delete=models.CASCADE, null=True)
    is_main = models.BooleanField(default=False)

    class Meta:
        unique_together = (('article', 'tag'),)


    def clean(self):
        if self.is_main and Scope.objects.filter(article=self.article, is_main=True).exists():
            raise ValidationError('only 1 tag for article')
