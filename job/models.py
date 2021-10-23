from django.db import models


class JobModel(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)
    salary = models.IntegerField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)