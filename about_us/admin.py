from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.

admin.site.register(AboutUs)
admin.site.register(Team)
admin.site.register(Testimonial)
admin.site.register(AboutUsContents)
@admin.register(AboutUsContentImage)
class AboutUsContentImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_preview', 'image')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />', obj.image.url)
        return 'No image'
    image_preview.short_description = 'Image Preview'