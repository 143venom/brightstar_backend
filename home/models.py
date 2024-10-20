from django.db import models
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
import sys
import logging

logger = logging.getLogger(__name__)

class Slider(models.Model):
    title = models.CharField(max_length=255)
    maintitle = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to="home/sliders/", default="home/sliders/default.jpg"
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        Resize and compress the image if it's new or updated.
        """
        if self.image and isinstance(self.image, InMemoryUploadedFile):
            try:
                img = Image.open(self.image)

                # Resize image
                target_size = (800, 800)
                img = img.resize(target_size, Image.Resampling.LANCZOS)

                # Prepare BytesIO for saving
                img_io = BytesIO()
                img_format = 'JPEG'  # Saving as JPEG for compression
                quality = 85

                # Save the image with initial quality
                img.save(img_io, format=img_format, quality=quality)
                img_io.seek(0)

                # Log initial size
                logger.debug(f"Initial image size: {img_io.tell()} bytes")

                # Reduce quality if the file size is too large
                while img_io.tell() > 3 * 1024 * 1024 and quality > 10:
                    img_io = BytesIO()
                    quality -= 5
                    img.save(img_io, format=img_format, quality=quality)
                    img_io.seek(0)

                    # Log each iteration size
                    logger.debug(f"Reducing quality to {quality}. Current size: {img_io.tell()} bytes")

                # Set the image to the resized and compressed image
                self.image = InMemoryUploadedFile(
                    img_io,
                    "ImageField",
                    self.image.name,
                    f"image/{img_format.lower()}",
                    img_io.tell(),  # Use tell() for the actual size
                    None,
                )

                # Log final size
                logger.debug(f"Final image size: {img_io.tell()} bytes")

            except Exception as e:
                logger.error(f"Error processing image: {e}")

        super().save(*args, **kwargs)


class Main(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="home/main/", default="home/main/default.jpg")

    def __str__(self):
        return self.title


# class AboutUsContentImage(models.Model):
#     image = models.ImageField(upload_to="home/about_us/", null=True, blank=True)


# class AboutUsContents(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     icon = models.CharField(max_length=255)


class ServiceSection(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Service(models.Model):
    services = models.ForeignKey(
        ServiceSection, related_name="services", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=255)  # For Font Awesome or Bootstrap icon class

    def __str__(self):
        return self.title


class NewsArticle(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    content = models.TextField()
    image = models.ImageField(upload_to="home/news/", default="home/news/default.jpg")

    def __str__(self):
        return self.title
