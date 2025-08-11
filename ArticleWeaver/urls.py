from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('<str:category>/<slug:slug>.html', views.article_detail, name='article_detail'),
]