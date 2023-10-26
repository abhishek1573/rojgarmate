from django.shortcuts import render
from client_jg.models import *

# Create your views here.

def index_page(request):
    return render(request, 'site_admin/html/index.html')

def admin_signup(request):
    pass

def view_job(request):
    crse=job_giver_details.objects.all()
    return render(request,'app1/adminpages/veiwcourseadmin.html',{'crse':crse})