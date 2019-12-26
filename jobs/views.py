from django.shortcuts import render, get_object_or_404
from .models import Job


def home(request):
    jobs = Job.objects
    return render(request,'jobs/home.html',{'jobs':jobs})

def pics(request):
    jobs = Job.objects
    return render(request,'jobs/jobs.html',{'jobs':jobs})
