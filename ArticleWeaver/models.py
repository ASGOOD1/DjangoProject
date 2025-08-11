from django.db import models
from django.utils.text import slugify

class Article(models.Model):
    CATEGORY_CHOICES = [
        ('fotbal-intern', 'Fotbal Intern'),
        ('fotbal-extern', 'Fotbal Extern'),
        ('tenis', 'Tenis'),
        ('alte', 'Alte Sporturi'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='alte')
    published_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
