from django.contrib import admin
from .models import *
from django.utils.html import format_html


# Register your models here.
@admin.register(ContactBackgroundImage)
class AboutUsContentImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_preview', 'image')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />', obj.image.url)
        return 'No image'
    image_preview.short_description = 'Image Preview'
admin.site.register(ContactFirstContent)
admin.site.register(ContactSecondContents)
admin.site.register(ContactForm)
admin.site.register(ContactUsInfo)

