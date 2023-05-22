from ast import Or
import email
from re import search
from turtle import home
from unicodedata import category
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.db.models import Q
from django.contrib import messages
import math
from .forms import JobForm
from datetime import datetime
from django.core.paginator import Paginator
from .filters import JobFilter
from django_filters import CharFilter
from django.urls import reverse


def Home(request):
    job = Job.objects.all().order_by('-id')
    company = Company.objects.all()
    # comp_id = company[0].id
    p = Paginator(Job.objects.all().order_by('-id'), 4)
    page = request.GET.get('page')
    jobs = p.get_page(page)
    a = 1
    b = jobs.number
    prvpage = b - a
    nextpage = a + b
    print(prvpage)
    
    

    
    username = "None"
    if prvpage == 0:
        prvpage = prvpage + a
        print(f'?page=',+ prvpage)
        return render(request, 'home/index.html',{
            'all_job': job,
            'jobs': jobs,
            'prvpage': prvpage,
            'nextpage': nextpage,
            # 'comp_id': comp_id
        })
    elif nextpage > b:
        pass

    # if request.session['is_user']:
    #     print("LOGIN SUCCESS",request.session['is_user'])
    #     username = request.session['username']
    # else:
    #     print("NOT LOGIN")

    return render(request, 'home/index.html', {
        'all_job': job,
        'company': company,
        'jobs': jobs,
        'prvpage': prvpage,
        'nextpage': nextpage,
        'username': username
    })

def MemberHome(request):
    
    job_recommend = JobFilter(queryset=request.session['education_category'])
  
 
    return render(request, 'member/index.html', {
        'jobs': job_recommend
    })


def ViewJob(request, job_id): # user is authenticated
    
    job = Job.objects.filter(id=job_id)
    comp = Company.objects.filter(compname=job[0].compname )
    description = comp[0].description
    email = comp[0].email
    phoneNumber = comp[0].phone
    address = comp[0].address
    job_apply = JobApply.objects.filter(Q(job_id=job_id) & Q(members=request.session['username']))
    print(job_apply)
        
    print(job)
    if len(job_apply) > 0:
        btnApply = False
    else:
        btnApply = True

    if job:
        for i in job:
            dateTime = i.posted_date.strftime("%b %d, %Y")
            print("After formatting:", dateTime)
            i.posted_date = dateTime
        return render(request, 'home/ViewJob.html', {
            'jobs': job,
            'description': description,
            'address': address,
            'email': email,
            'phoneNumber': phoneNumber,
            'btnApply': btnApply
            
        })
    else:
        return render(request, 'home/ViewJob.html', {
            "jobs": None,
            "all_job": None,
        })

def View(request, job_id): # user not is authenticated
    
    job = Job.objects.filter(id=job_id)

    entrepre = Company.objects.filter(compname=job[0].compname )
    description = entrepre[0].description
    address = entrepre[0].address
    email =entrepre[0].email
    phoneNumber = entrepre[0].phone
    btnApply = False
    print('เกี่ยวกับ',entrepre)

    if job:
        for i in job:
            dateTime = i.posted_date.strftime("%b %d, %Y")
            print("After formatting:", dateTime)
            i.posted_date = dateTime
        return render(request, 'home/ViewJob.html', {
            'jobs': job,
            # 'entrepreneur': entrepre,
            'email': email,
            'phoneNumber': phoneNumber,
            'description': description,
            'address': address,
            'btnApply': btnApply
            
        })
    else:
        return render(request, 'home/ViewJob.html', {
            "jobs": job,
            # "entrepreneur": entrepre,
            

        })


def Login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user_find = User.objects.filter(email=email)

        user = authenticate(request, username=user_find[0].username, password=password)
        for i in user_find:
            print("USER", i.is_active)
            if i.is_active == True:
                request.session['is_user'] = i.is_active
                request.session['username'] = i.username
                request.session['email'] = i.email
                
            else:
                pass

        if user is not None:  # login success
            login(request, user)
            print(user)
            return redirect('/')
        elif user:
            logout(request)
            messages.success(request, ("Logout Success"))
            return redirect('login')
        else:
            messages.success(request, ("There was An Error Logging In, Try Again..."))
            return redirect('login')
    else:
        return render(request, 'home/login.html')


def CompRegister(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        compname = request.POST['compname']
        category = request.POST['category']
        address = request.POST['address']
        phone = request.POST['phone']
        logo = request.FILES['logo']
        print(email, password, compname, category, address, phone)
        entrepre = Company.objects.filter(
            Q(compname=compname) | Q(email=email))
        print(entrepre)
        if entrepre:
            messages.success(request, ("มีชื่อบริษัทหรืออีเมลนี้ในระบบแล้ว, โปรดลองอีกครั้ง..."))
            return redirect('/CompRegister')
        else:
            entrepre = Company.objects.create(
                compname=compname, password=password, email=email, category=category, address=address, phone=phone, logo=logo)
            entrepre.save()
            user = User.objects.create_user(
                username=compname, password=password, email=email, is_active=True, is_staff=True
            )
            user.save()
            return redirect('login')
    else:
        return render(request, 'home/CompRegister.html')


def MemberRegister(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        member = Member.objects.filter(Q(email=email) | Q(username=username))
      
        if member:
            messages.success(request, ("ชื่อหรืออีเมลนี้ได้สมัครเป็นสมาชิกแล้ว, โปรดลองอีกครั้ง..."))
            return redirect('/MemberRegister')
        else:
            member = Member.objects.create(
                username=username, email=email, password=password)
            member.save()
            user = User.objects.create_user(
                username=username, password=password, email=email, is_active=True, is_staff=False
            )
            user.save()
            messages.success(request, ("สมัครสำเร็จ"))
            return redirect('login')
    else:
        return render(request, 'home/MemberRegister.html')


def FindJob(request):
    job = Job.objects.all().order_by('-id')

    myFilter = JobFilter(request.GET, queryset=job)
    jobs = myFilter.qs
    print('ผลลัพธ์ค้นหา',jobs[0].compname,jobs[0].type)
    
    p = Paginator(jobs.order_by('-id'), 10)
    page = request.GET.get('page')
    jobs_limit = p.get_page(page)
    a = 1
    b = jobs_limit.number
    prvpage = b - a
    nextpage = a + b

    if prvpage == 0:
        prvpage = prvpage + a
        print(f'?page=',+ prvpage)
        # return redirect(f'FindJob?compname={jobs[0].compname}&position={jobs[0].position}&category={jobs[0].category}&property={jobs[0].property}&description={jobs[0].description}&type={jobs[0].type}'
        return render(request,'home/FindJob.html',{
            'jobs': jobs,
            'job': job,
            'jobs_limit': jobs_limit,
            'prvpage': prvpage,
            'nextpage': nextpage,
            'myFilter': myFilter
        })
    else:
        pass


    return render(request,'home/FindJob.html', {
        'jobs': jobs,
        'job': job,
        'jobs_limit': jobs_limit,
        'prvpage': prvpage,
        'nextpage': nextpage,
        'myFilter': myFilter
    })


def Test(request):

    return render(request, 'home/Test.html')


