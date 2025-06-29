from rest_framework import viewsets, permissions
from .models import Post
from .serializers import PostSerializer
from .services import PostService

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        post = serializer.save(author=self.request.user)
        PostService().publish_post_created(post)