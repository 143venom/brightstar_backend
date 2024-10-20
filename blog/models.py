from django.db import models
from readtime import of_text

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    post_image = models.ImageField(
        upload_to="blogs/post_img", default="blogs/post_img/post.jpg"
    )
    author = models.CharField(max_length=200)
    author_image = models.ImageField(
        upload_to="blogs/author_img", default="blogs/author_img/author.jpg"
    )
    published_at = models.DateTimeField(auto_now_add=True)
    facebook_url = models.URLField(blank=True, null=True)
    linkind_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def read_time(self):
        return of_text(self.content).text
