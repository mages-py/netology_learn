from django.db import models


class Tag(models.Model):
    name  = models.CharField(max_length=200, verbose_name='Название')
    
    class Meta:
        verbose_name  =  'Категория'
        verbose_name_plural   =   'Категории'
    
    def __str__(self):
        return self.name

class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    tags   = models.ManyToManyField(Tag, related_name='articles', through='Scope')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class Scope(models.Model):
    article  = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья', related_name='scopes')
    tag   = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='Категория', related_name='scopes')
    is_main  = models.BooleanField(default=False, verbose_name='Основная')
    
    class Meta:
        verbose_name  =  'Категория'
        verbose_name_plural   =   'Категории'
        ordering = ['-is_main', 'tag__name']