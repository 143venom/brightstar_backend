from django.db import models
from core.models import BaseModel
from core.models import CustomUser

User = CustomUser


class PersonalDetails(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Education(BaseModel):
    cv = models.ForeignKey("CV", related_name="education", on_delete=models.CASCADE)
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()


class Experience(BaseModel):
    cv = models.ForeignKey("CV", related_name="experience", on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()


class Skill(BaseModel):
    cv = models.ForeignKey("CV", related_name="skills", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50)


class CV(BaseModel):
    personal_details = models.OneToOneField(PersonalDetails, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
