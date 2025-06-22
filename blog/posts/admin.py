from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        ('SEO', {
            'fields': ('seo_title', 'meta_description', 'og_image', 'canonical_url'),
            'classes': ('collapse',)
        }),
        ('Основное', {
            'fields': ('title', 'slug', 'content', 'author')
        }),
        ('Дополнительно', {
            'fields': ('published_at', 'views', 'template', 'status')
        }),
    )
    list_display = ('title', 'author', 'published_at', 'status')
    search_fields = ('title', 'content')