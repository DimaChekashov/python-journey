from django.db import models
from django.contrib.auth.models import User
from datetime import date

class SEO(models.Model):
    title = models.CharField(max_length=255)
    meta_description = models.TextField()
    og_image = models.ImageField(upload_to='uploads/')
    canonical_url= models.CharField(max_length=255)

class Post(models.Model):
    TEMPLATE_CHOICES = [
        {'blue', 'Синий'},
        {'green', 'Зеленый'},
        {'red', 'Красный'}
    ]
    STATUS_CHOICES = [
        {'opened', 'Открыто'},
        {'closed', 'Закрыто'},
        {'archived', 'В архиве'}
    ]

    seo = models.OneToOneField(SEO, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    published_at = models.DateField(default=date.today)
    author = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    template = models.CharField(max_length=50, choices=TEMPLATE_CHOICES)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    # author = models.ForeignKey(User, on_delete=models.CASCADE)
