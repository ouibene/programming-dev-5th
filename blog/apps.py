from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'

class PostConfig(AppConfig):
    name = 'post_list'

class CommentsConfig(AppConfig):
    name = 'comment'