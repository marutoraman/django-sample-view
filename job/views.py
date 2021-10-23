from django.shortcuts import render
from django.views.generic import TemplateView

from .models import JobModel

# Create your views here.

class JobView(TemplateView):
    template_name = "job/list.html"
    
    def get(self, request):
        jobs = JobModel.objects.all()
        return self.render_to_response({
            "jobs": jobs,
            "sample1": "サンプル１",
            "sample2": "サンプル２"
        })
        
        
class JobDetailView(TemplateView):
    template_name = "job/detail.html"
    
    def get(self, request):
        job = JobModel.objects.filter(id=request.GET.get("id")).first()
        return self.render_to_response({
            "job": job
        })