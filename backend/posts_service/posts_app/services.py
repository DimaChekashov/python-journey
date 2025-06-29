from .producers import PostProducer

class PostService:
    def __init__(self):
        self.producer = PostProducer()

    def publish_post_created(self, post):
        self.producer.send_post_created({
            'id': post.id,
            'title': post.title,
            'author_id': post.author.id,
            'created_at': post.created_at.isoformat()
        })