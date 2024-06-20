from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True,
                              verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')
    articles  = models.ManyToManyField(Article, through='Score')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Score(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scores')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scores')
    is_main = models.BooleanField(default=False)
