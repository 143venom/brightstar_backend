from rest_framework import serializers
from .models import CV, PersonalDetails, Education, Experience, Skill


class PersonalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalDetails
        exclude = ['created_at', 'updated_at']


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        exclude = ['created_at', 'updated_at']


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        exclude = ['created_at', 'updated_at']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        exclude = ['created_at', 'updated_at']


class CVSerializer(serializers.ModelSerializer):
    personal_details = PersonalDetailsSerializer()
    education = EducationSerializer(many=True)
    experience = ExperienceSerializer(many=True)
    skills = SkillSerializer(many=True)

    class Meta:
        model = CV
        exclude = ['created_at', 'updated_at']
