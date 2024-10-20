from rest_framework import serializers
from .models import *


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"


class AboutUsContentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsContents
        fields = "__all__"


class AboutUsContentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsContentImage
        fields = "__all__"
