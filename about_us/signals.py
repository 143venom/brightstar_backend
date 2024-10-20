# signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import AboutUs
from job.models import Jobs

@receiver(post_save, sender=Jobs)
@receiver(post_delete, sender=Jobs)
def update_about_us(sender, **kwargs):
    try:
        about_us = AboutUs.objects.first()  # Assumes there is only one AboutUs instance
        if about_us:
            # Update job count
            total_jobs = Jobs.objects.count()
            about_us.jobs_found_count = str(total_jobs)
            
            # Update recruiters count
            recruiters_count = Jobs.objects.values('company_name').distinct().count()
            about_us.recruiters_count = str(recruiters_count)
            
            about_us.save()
    except AboutUs.DoesNotExist:
        pass
