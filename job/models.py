from django.db import models
from django.core.exceptions import ValidationError
from core.models import BaseModel, CustomUser
from country.models import Country
from about_us.models import AboutUs


class Job_Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Job_Level(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Job_Type(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Job_Location(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Job_Education_Level(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Jobs(BaseModel):
    PUBLISHED = "PU"
    UNPUBLISHED = "UN"
    STATUS_CHOICES = [
        (PUBLISHED, "Published"),
        (UNPUBLISHED, "Unpublished"),
    ]

    company_profile_pic = models.ImageField(
        upload_to="images/job/company_profile_pic/", blank=True, null=True
    )
    company_cover_pic = models.ImageField(
        upload_to="images/job/company_cover_pic/", blank=True, null=True
    )
    company_description = models.TextField(blank=True, null=True)
    job_title = models.CharField(max_length=255, blank=True, null=True)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, blank=True, null=True
    )
    job_category = models.ForeignKey(
        Job_Category, on_delete=models.CASCADE, blank=True, null=True
    )
    job_level = models.ForeignKey(
        Job_Level, on_delete=models.CASCADE, blank=True, null=True
    )
    vacancy = models.IntegerField()
    job_types = models.ForeignKey(
        Job_Type, on_delete=models.CASCADE, blank=True, null=True
    )
    job_location = models.ForeignKey(
        Job_Location, on_delete=models.CASCADE, blank=True, null=True
    )
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    company_name = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    education = models.ForeignKey(
        Job_Education_Level, on_delete=models.CASCADE, blank=True, null=True
    )
    job_description = models.TextField(blank=True, null=True)
    responsibilities = models.TextField(blank=True, null=True, max_length=500)
    requirements = models.TextField(blank=True, null=True, max_length=1000)
    preferred_qualifications = models.TextField(blank=True, null=True, max_length=500)
    why_join_us = models.TextField(blank=True, null=True, max_length=500)
    job_status = models.CharField(
        max_length=2,
        blank=False,
        null=False,
        choices=STATUS_CHOICES,
        default=PUBLISHED,
        verbose_name="Status",
        db_index=True,
    )
    valid_until = models.DateTimeField()

    def __str__(self):
        return self.job_title
    
    def count_jobs(self):
        return Jobs.objects.count()

    def count_recruiters(self):
        return Jobs.objects.values('company_name').distinct().count()

    def save(self, *args, **kwargs):
        AboutUs.jobs_found_count = self.count_jobs()
        AboutUs.recruiters_count = self.count_recruiters()
        super().save(*args, **kwargs)
    

class JobApplication(BaseModel):
    job = models.ForeignKey(Jobs, related_name='applications', on_delete=models.CASCADE)
    applicant_name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to='images/job/resumes/')
    cover_letter = models.FileField(upload_to='images/job/resumes/cover_letter')
    application_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant_name} - {self.job.job_title}"
