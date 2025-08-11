from django.shortcuts import render, get_object_or_404
from .models import Article

def article_list(request):
    articles = Article.objects.order_by('-published_at')
    return render(request, 'articles/article_list.html', {'articles': articles})
def article_detail(request, category, slug):
    article = get_object_or_404(Article, category=category, slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})
