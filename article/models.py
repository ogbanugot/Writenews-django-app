from django.db import models
from django.utils import timezone
from django.conf import settings  

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='article', on_delete=models.CASCADE)
    article_name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    category = models.CharField(max_length=255, default=None)
    uploaded = models.DateTimeField(default=timezone.now, blank=True)
    
    class Meta:
        ordering = ('uploaded',)
