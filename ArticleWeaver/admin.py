from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'is_featured', 'published_at')
    list_filter = ('category', 'status', 'is_featured', 'published_at')
    search_fields = ('title', 'summary', 'content')
    ordering = ('-published_at',)
    prepopulated_fields = {"slug": ("title",)}  # Optional, for manual slug edits

    def has_delete_permission(self, request, obj=None):
        return True
