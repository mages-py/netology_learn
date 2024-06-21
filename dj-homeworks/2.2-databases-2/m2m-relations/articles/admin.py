
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag

class ScopeInlineFormSet(BaseInlineFormSet):
    def clean(self):
        tags = [form.cleaned_data for form in self.forms]
        print(tags)
        qty_main_tags = len([x for x in tags if x['is_main'] and not x['DELETE']])
        if qty_main_tags > 1:
            raise ValidationError("Основной может быть только одна категория")
        elif qty_main_tags == 0:
            raise ValidationError("Выберите категорию в качестве основной")
        return super().clean()

class ScopeAdmin(admin.TabularInline):
    model = Scope
    extra =   0
    formset =  ScopeInlineFormSet

    
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title']
    list_filter =  ['published_at']
    inlines = [ScopeAdmin]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display  = ['id','name']

