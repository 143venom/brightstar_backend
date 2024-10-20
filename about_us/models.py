from django.db import models
from core.models import BaseModel

# Create your models here.

class AboutUsBackgroundImage(BaseModel):
    image = models.ImageField(
        upload_to="images/about_us/background_images/",
        default="https://t3.ftcdn.net/jpg/05/30/96/04/240_F_530960431_c8fPd3HansYvrSJ4fJxZqp9OhjQmYoll.jpg",
    )


def __str__(self):
    return f"Contact Background Image (URL: {self.image.url})"

class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="about", default="about/default.jpg")
    jobs_found_count = models.CharField(max_length=100, default=2)
    recruiters_count = models.CharField(max_length=100)

    def __str__(self):
        return self.title


# class AboutUsContentlist(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField(max_length=255)

#     def __str__(self):
#         return f"{self.title} {self.content}"


class AboutUsContentImage(models.Model):
    image = models.ImageField(
        upload_to="images/about_us/aboutuscontent/image", null=True, blank=True
    )

    # def __str__(self):
    #     return self.image.url


class AboutUsContents(models.Model):
    icon = models.ImageField(
        upload_to="images/about_us/aboutuscontent/icon/", null=True, blank=True
    )
    title = models.CharField(max_length=255)
    description = models.TextField()


class Team(models.Model):
    name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="team/", default="team/default.jpg")

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(
        upload_to="testimonial/", default="testimonial/default.jpg"
    )

    def __str__(self):
        return self.name
