from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Post(models.Model):
    TEMPLATE_CHOICES = [
        ('blue', 'Синий'),
        ('green', 'Зеленый'),
        ('red', 'Красный')
    ]
    STATUS_CHOICES = [
        ('opened', 'Открыто'),
        ('closed', 'Закрыто'),
        ('archived', 'В архиве')
    ]
    
    seo_title = models.CharField('SEO Title', max_length=255, blank=True)
    meta_description = models.TextField('Meta Description', blank=True)
    og_image = models.ImageField('OpenGraph Image', upload_to='uploads/', blank=True)
    canonical_url = models.CharField('Canonical URL', max_length=255, blank=True)

    title = models.CharField('Заголовок', max_length=200)
    slug = models.SlugField('URL-адрес', unique=True)
    content = models.TextField('Содержание')
    published_at = models.DateField('Дата публикации', default=date.today)
    author = models.CharField('Автор', max_length=100)
    views = models.IntegerField('Просмотры', default=0)
    template = models.CharField('Шаблон', max_length=50, choices=TEMPLATE_CHOICES)
    status = models.CharField('Статус', max_length=50, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
