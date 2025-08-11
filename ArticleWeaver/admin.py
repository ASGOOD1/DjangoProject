from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'category')
    search_fields = ('title', 'content')
    list_filter = ('category', 'published_at')
    ordering = ('-published_at',)

    def has_delete_permission(self, request, obj=None):
        return True
