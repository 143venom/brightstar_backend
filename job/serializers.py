from rest_framework import serializers
from .models import Jobs
from rest_framework import serializers
from .models import *
from country.serializers import CountrysSerializer


class JobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_Category
        fields = "__all__"


class JobLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_Level
        fields = "__all__"


class JobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_Type
        fields = "__all__"


class JobLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_Location
        fields = "__all__"


class JobEducationLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_Education_Level
        fields = "__all__"


class JobsSerializer(serializers.ModelSerializer):
    country = CountrysSerializer()
    job_category = JobCategorySerializer()
    job_level = JobLevelSerializer()
    job_types = JobTypeSerializer()
    job_location = JobLocationSerializer()
    education = JobEducationLevelSerializer()
    class Meta:
        model = Jobs
        fields = "__all__"


class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = "__all__"
