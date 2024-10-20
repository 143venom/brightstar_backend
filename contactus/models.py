from django.db import models
from core.models import BaseModel


# Create your models here.
class ContactBackgroundImage(BaseModel):
    image = models.ImageField(
        upload_to="images/contact/background_images/",
        default="https://t3.ftcdn.net/jpg/05/30/96/04/240_F_530960431_c8fPd3HansYvrSJ4fJxZqp9OhjQmYoll.jpg",
    )


def __str__(self):
    return f"Contact Background Image (URL: {self.image.url})"


class ContactFirstContent(BaseModel):
    title_one = models.CharField(max_length=255, default='need to change title_one')
    title_two = models.CharField(max_length=255, default='need to change title_two')
    content = models.CharField(max_length=1000)

    def __str__(self):
        return f"title_one: {self.title_one}title_two: {self.title_two}content: {self.content}"


class ContactSecondContents(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class ContactForm(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ContactUsInfo(BaseModel):
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.address} {self.phone_number} {self.email}"
