import email
from itertools import count
from operator import length_hint
from turtle import home
from unicodedata import category
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db.models import Q
import math
from datetime import datetime
from django.core.paginator import Paginator


from home.models import *


def Home(request):
    job = Job.objects.all().order_by('-id')
    company = Company.objects.all()
    print('ID',company[2].compname)
    # comp_id = company[0].id
    p = Paginator(Job.objects.all().order_by('-id'), 10)
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
        return render(request, 'member/index.html',{
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

    return render(request, '/index.html', {
        'all_job': job,
        'company': company,
        'jobs': jobs,
        'prvpage': prvpage,
        'nextpage': nextpage,
        'username': username
    })


def Apply(request,job_id):
    members = request.session['username']  

    member = Member.objects.filter(username=members)
    job = Job.objects.filter(id=job_id)
    
    apply_date = datetime.now()
    print('สมัครเวลา',apply_date)

    job_apply = JobApply.objects.create(
        members=members,compname=job[0].compname, position=job[0].position, member_id=member[0].id, job_id=job[0].id, apply_date=apply_date
    )
    print('สมัครงานตำแหน่ง :',job[0].position, 'บริษัท :',job[0].compname
    )
    job_apply.save()

    return redirect(f'/{job_id}')

def CancelApply(request, job_id):
    job_apply = JobApply.objects.filter(Q(job_id=job_id) & Q(members=request.session['username']))

    if request.method == "POST":
        print('ยกเลิกการสมัครสำเร็จ')
        job_apply.delete()
    
    return redirect(f'/{job_id}')

def ListApply(request):
    listApply = JobApply.objects.filter(members=request.session['username'])
    p = Paginator(JobApply.objects.filter(members=request.session['username']), 10)
    page = request.GET.get('page')
    list_apply = p.get_page(page)
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    a = 1
    b = list_apply.number
    prvpage = b - a
    nextpage = a + b

    if prvpage == 0:
        prvpage = prvpage + a
        print(f'?page=',+ prvpage)
        
        return render(request, 'member/ListApply.html',{
            'list': listApply,
            'list_apply': list_apply,
            'prvpage': prvpage,
            'nextpage': nextpage,
        })

    print("Current time in Asia/Bangkok is: ", time)
    if listApply:
        for time in listApply:
            apply_date = time
            print("After formatting:", apply_date)
            time = apply_date
            return render(request, 'member/ListApply.html', {
                'list': listApply,
                'list_apply': list_apply,
                'prvpage': prvpage,
                'nextpage': nextpage,
                            
            })
    return render(request, 'member/ListApply.html', {
            'list': listApply,
            'list_apply': list_apply,
                         
        })

def ProfileMember(request):
    email =  request.session['email']
    print(email)
    if request.method == "GET":
        try:
            member = Member.objects.get(email=email)
            
        except:
            pass

        return render(request,'member/ProfileMember.html',{
            'member': member,
            
            
        })

    if request.method == "POST": 
        member = Member.objects.get(email=email)
        print(member)
        username = member.username
        member.name_th = request.POST['name_th']
        member.name_eng = request.POST['name_eng']
        member.birth_day = request.POST['birth_day']
        member.sex = request.POST['sex']
        member.email = member.email
        member.nationality = request.POST['nationality']
        member.religion = request.POST['religion']
        member.phone = request.POST['phone']
        member.school = request.POST['school']
        member.education_level = request.POST['education_level']
        member.faculty = request.POST['faculty']
        member.major = request.POST['major']
        member.education_category = request.POST['education_category']
        member.state = request.POST['state']
        member.year = request.POST['year']
        member.gpa = request.POST['gpa']
        
        member.save()
   
    return render(request,'Member/ProfileMember.html',{
      'member': member,
      'username': username,
    })
         
