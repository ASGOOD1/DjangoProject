from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Article


def article_list(request):
    """
    Acts as the homepage.
    - picks one featured article as HERO
    - lists the latest published articles (excludes the hero)
    - paginates the rest
    """
    # hero (optional)
    hero = (
        Article.objects.filter(status="pub", is_featured=True)
        .order_by("-published_at")
        .first()
    )

    # latest (published only)
    qs = Article.objects.filter(status="pub").order_by("-published_at")
    if hero:
        qs = qs.exclude(pk=hero.pk)

    articles = Paginator(qs, 9).get_page(request.GET.get("page", 1))

    return render(
        request,
        "articles/article_list.html",
        {"hero": hero, "articles": articles},
    )


def article_detail(request, category, slug):
    """
    Detail page constrained to published articles
    and matching category/slug.
    """
    article = get_object_or_404(
        Article, status="pub", category=category, slug=slug
    )
    return render(request, "articles/article_detail.html", {"article": article})
