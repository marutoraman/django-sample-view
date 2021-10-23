from django.contrib import admin

from .models import JobModel

@admin.register(JobModel)
class JobModel(admin.ModelAdmin):
    pass