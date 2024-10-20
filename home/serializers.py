from rest_framework import serializers
from .models import *


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'


class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = '__all__'

# class AboutUsContentsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AboutUsContents
#         fields = '__all__'


# class AboutUsContentImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AboutUsContentImage
#         fields = '__all__'


class ServiceSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceSection
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class NewsArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticle
        fields = '__all__'
