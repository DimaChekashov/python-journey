from rest_framework import serializers
from .models import Post
from django.conf import settings

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        extra_kwargs = {
            'slug': {'read_only': True},
            'views': {'read_only': True}
        }

    def to_representation(self, instance):
        # Получаем базовое представление
        data = super().to_representation(instance)
        
        # Формируем полный URL для изображения
        og_image_url = None
        if instance.og_image:
            request = self.context.get('request')
            og_image_url = request.build_absolute_uri(instance.og_image.url) if request else f"{settings.BASE_URL}{instance.og_image.url}"

        return {
            "id": instance.slug,
            "seo": {
                "title": data['seo_title'],
                "meta_description": data['meta_description'],
                "og_image": og_image_url,
                "canonical_url": data['canonical_url']
            },
            "data": {
                "id": data['id'],
                "title": data['title'],
                "slug": data['slug'],
                "content": data['content'],
                "published_at": data['published_at'],
                "author": data['author'],
                "views": data['views']
            },
            "template": data['template'],
            "status": data['status']
        }