from django.contrib import admin

from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        super().clean()
        main_scope_count = 0
        for form in self.forms:
            if form.cleaned_data and form.cleaned_data.get('is_main'):
                main_scope_count += 1
        if main_scope_count > 1:
            raise ValidationError('only 1 tag for article')


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 3

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']


