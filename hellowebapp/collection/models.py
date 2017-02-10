from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Quote(models.Model):
    author = models.CharField(max_length=255)
    blockquote = models.TextField()
    source = models.URLField(max_length=220)
    slug = models.SlugField(unique=True)
    user = models.OneToOneField(User, blank=True, null=True)
    
    