import email
from email.mime import image
from turtle import home
from unicodedata import category
from urllib.request import Request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db.models import Q
import math
from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator

from django.shortcuts import render, redirect

from home.models import *
from home.forms import JobForm, ImageForm
import member
from home.filters import JobFilter


def Myjob(request):
    compname = request.session['username']
    all_job = Job.objects.filter(compname=compname).order_by('-id')
    p = Paginator(Job.objects.filter(compname=compname).order_by('-id'),15)
    page = request.GET.get('page')
    jobs = p.get_page(page)
    a = 1
    b = jobs.number
    prvpage = b - a
    nextpage = a + b
    company = Company.objects.get(compname=compname)
    category = company.category
    logo = company.logo
    print(category)

    myFilter = JobFilter(request.GET, queryset=all_job)
    job_filter = myFilter.qs
    if prvpage == 0:
        prvpage = prvpage + a
        print(f'?page=',+ prvpage)
        return render(request, 'company/myjob.html',{
            'job' : all_job,
            'job_filter' : job_filter,
            'myFilter' : myFilter,
            'compname': compname,
            'logo': logo,
            'jobs': jobs,
            'prvpage': prvpage,
            'nextpage': nextpage,
        })
    return render(request, 'company/myjob.html', {
        'job' : all_job,
        'jobs': jobs,
        'logo': logo,
        'compname': compname,
        'prvpage': prvpage,
        'nextpage': nextpage,
        
        })

def Create_Job(request):
    compname = request.session['username']
    company = Company.objects.get(compname=compname)
    category = company.category
    logo = company.logo
    print(logo)
    if request.method == "POST":
        category = category
        position = request.POST['position']
        salary = request.POST['salary']
        quantity = request.POST['quantity']
        type = request.POST['type']
        logo = logo
        gpa = request.POST['gpa']
        description = request.POST['description']
        property = request.POST['property']
        welfare = request.POST['welfare']
        experience = request.POST['experience']
        working_time = request.POST['working_time']



        posted_date = datetime.utcnow()
        job = Job.objects.filter(position=position)

        if job:
            messages.success(request, ("ตำแหน่งนี้เคยลงประกาศแล้ว, โปรดระบุตำแหน่งใหม่..."))
            return redirect('/CreateJob')

        else:
            job = Job.objects.create(
                position=position,category=category, salary=salary, quantity=quantity, type=type, logo=logo, gpa=gpa,
                description=description, property=property, welfare=welfare, experience=experience, posted_date=posted_date,
                working_time=working_time,compname=compname)
            print(job)
            job.save()
            
        return redirect('/myjob')

    elif request.method == "GET":

        form = ImageForm()
        compname = request.session['username']

        return render(request, 'company/CreateJob.html', {
            'jobForm': form,
            'compname': compname,
            'form': form
        })


def update_image_job(request, job_id):

    if request.method == "POST":
        job = Job.objects.get(id=job_id)
        
        job.logo = request.FILES['logo']

        print(job.logo)
        
        job.save()

        return redirect('/myjob', {
            'jobs': job,

        })

def update_image(request):

    email = request.session['email'] 
    compname = request.session['username'] 
    if request.method == "POST":
        comp = Company.objects.get(email=email)
        job = Job.objects.get(compname=compname)

        comp.logo = request.FILES['logo']
        job.logo = request.FILES['logo']

        print( comp.logo)
        
        comp.save()
        job.save()

        return redirect('/Profile', {
            'comp':  comp,
            'job': job,

        })
     

def edit_job(request, job_id):
    if request.method == "GET":
        try:
            job = Job.objects.get(id=job_id)
            form = ImageForm()
            print(job)
            
        except:
            pass

        return render(request, 'company/job_edit.html', {
            "jobs": job,
            "form": form,
        })
    
    if request.method == "POST":
        job = Job.objects.get(id=job_id)

        job.category = request.POST['category']
        job.position = request.POST['position']
        job.salary = request.POST['salary']
        job.quantity = request.POST['quantity']
        job.type = request.POST['type']
    
        job.gpa = request.POST['gpa']   
        job.description = request.POST['description']
        job.property = request.POST['property']
        job.welfare = request.POST['welfare']
        job.experience = request.POST['experience']
        job.working_time = request.POST['working_time']
        
        job.posted_date = datetime.utcnow()
        
        # job = Job.objects.filter(position=job.position)

        # if job:
        #     messages.success(request, ("ตำแหน่งนี้เคยลงประกาศแล้ว, โปรดระบุตำแหน่งใหม่..."))
        #     return redirect(f'/{job_id}/Edit')

        # else:
        #     job = Job.objects.update(
        #         position=job.position,category=job.category, salary=job.salary, quantity=job.quantity, type=job.type, gpa=job.gpa,
        #         description=job.description, property=job.property, welfare=job.welfare, experience=job.experience, posted_date=job.posted_date,
        #         working_time=job.working_time)
        job.save()

        return redirect('/myjob', {
            'jobs': job,
            
            
        })

def Delete_Job(request, job_id):

    job = Job.objects.filter(id=job_id)
    members = JobApply.objects.filter(job_id=job_id)
    
    print(job)
    if request.method == "POST":
        members.delete()
        job.delete()
        

    return redirect('/myjob')

def Delete_Volunteer(request, jobapply_id, Job_id):
    
    apply = JobApply.objects.filter(id=jobapply_id)
    if request.method == "POST":
        apply.delete()
    
    return redirect(f'/views/{Job_id}')

def View_Apply(request, job_id):
    compname = request.session['username'] 
    job = Job.objects.filter(id=job_id)
    job_apply = JobApply.objects.filter(Q(compname=compname) & Q(position=job[0].position))
    all_job = Job.objects.filter(compname=compname)
    position = job[0].position
    company = Company.objects.get(compname=compname)
    logo = company.logo
    
    if len(job_apply) > 0:
       
        return render(request, 'company/view_apply.html', {
            'jobs': job, 
            'logo': logo, 
            'position': position,
            'all_job': all_job, 
            'list_apply': job_apply
        })
    else:
        return render(request, 'company/view_apply.html', {
            "jobs": job,
            "logo": logo,
            'position': position,
            'all_job': all_job, 
            'list__apply': job_apply
        })



def Update_Profile(request):
    compname = request.session['username']
    company = Company.objects.filter(compname=compname)
    update_company = Company.objects.filter(Q(id=company[0].id) & Q(compname=compname))
    
    print(company[0].id)

    return render('company/Profile.html', {
        'company': update_company
        
    })

def Profile(request):
    
    email = request.session['email'] 
    print(email)
    if request.method == "GET":
        try:
            comp = Company.objects.get(email=email)
            print(comp)
            comp.compname = comp[0].compname
            comp.email = comp[0].email
            comp.categoryl = comp[0].category
            comp.phone = comp[0].phone
            comp.description = comp[0].description
            comp.address = comp[0].address
            print(comp.email)
        except:
            pass

        return render(request,'company/Profile.html',{
            'comp': comp
            
        })


    if request.method == "POST":
        comp = Company.objects.get(email=email)
        user = User.objects.get(email=email)

        comp.compname = request.POST['compname']
        comp.category = request.POST['category']
        comp.phone = request.POST['phone']
        comp.description = request.POST['description']
        comp.email = comp.email
        comp.address = request.POST['address']
        user.username = comp.compname

        comp.save()
        user.save()
        return render(request,'company/Profile.html',{
            'comp': comp,
            'category': category,
        })

        
def ProfileApply(request, member_id):
    
    member = Member.objects.get(id=member_id)
    Th_Name = member.name_th
    
    print('ชื่อไทย',Th_Name)
    
    return render(request,'company/ProfileApply.html',{
        'member': member,
    })

