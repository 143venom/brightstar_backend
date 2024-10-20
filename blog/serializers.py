from rest_framework import serializers
from .models import *


class BlogPostSerializer(serializers.ModelSerializer):
    read_time = serializers.ReadOnlyField()

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'post_image', 'author', 'author_image', 'published_at', 'read_time']


class RecentBlogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'title', 'content', 'post_image', 'author', 'author_image', 'published_at', 'read_time']
        