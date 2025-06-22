from rest_framework import serializers
from .models import Post, SEO

class SEOSerializer(serializers.ModelSerializer):
    class Meta:
        model = SEO
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    seo = SEOSerializer()

    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {
            "id": instance.slug,
            "seo": {
                "title": data['seo']['title'],
                "meta_description": data['seo']['meta_description'],
                "og_image": data['seo']['og_image'],
                "canonicial_url": data['seo']['canonicial_url']
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
