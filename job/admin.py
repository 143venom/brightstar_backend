from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Jobs)
admin.site.register(Job_Category)
admin.site.register(Job_Level)
admin.site.register(Job_Type)
admin.site.register(Job_Location)
admin.site.register(Job_Education_Level)
admin.site.register(JobApplication)
