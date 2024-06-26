from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'
    articles  =  Article.objects.prefetch_related('tags').order_by(ordering).all()
    context = {'object_list': articles}
    return render(request, template, context)
