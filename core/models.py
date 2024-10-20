from django.db import models
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
import sys
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from random import randint
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


class CustomUser(AbstractUser, BaseModel):
    email = models.EmailField(unique=True, verbose_name="Email", max_length=255)
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone_number", "address"]
    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if not self.username:
            username_base = self.email.split("@")[0]
            username = username_base
            counter = 1
            while CustomUser.objects.filter(username=username).exists():
                username = f"{username_base}{counter}"
                counter += 1
            self.username = username
        super().save(*args, **kwargs)

    def __str__(self):
        return self.first_name

    def __str__(self):
        return self.first_name if self.first_name else self.email
    

class ImageResizeMixin:
    def save(self, *args, target_size=(800, 800), max_file_size=3 * 1024 * 1024, initial_quality=85, **kwargs):
        if hasattr(self, 'image') and self.image and isinstance(self.image, InMemoryUploadedFile):
            img = Image.open(self.image)

            # Resize image
            img = img.resize(target_size, Image.Resampling.LANCZOS)
            img_io = BytesIO()
            img_format = img.format if img.format else "JPEG"
            quality = initial_quality
            
            # Save the image with initial quality
            img.save(img_io, format='JPEG', quality=quality)
            img_io.seek(0)

            # Reduce quality if the file size is too large
            while img_io.tell() > max_file_size and quality > 10:
                img_io = BytesIO()
                quality -= 5
                img.save(img_io, format='JPEG', quality=quality)
                img_io.seek(0)

            self.image = InMemoryUploadedFile(
                img_io,
                "ImageField",
                self.image.name,
                "image/jpeg",  # Changed to 'image/jpeg' for consistent output
                sys.getsizeof(img_io),
                None,
            )

        super().save(*args, **kwargs)
