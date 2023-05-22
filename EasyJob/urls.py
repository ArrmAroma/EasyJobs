from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from home import views as HomeViews
from company import views as CompViews
from member import views as MemViews



urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('home.urls')),
    path('', HomeViews.Home),
    path('FindJob',HomeViews.FindJob, name='findjob'),
    path('login',HomeViews.Login, name='login'),
    path('MemberRegister',HomeViews.MemberRegister, name='register'),
    path('CompRegister',HomeViews.CompRegister, name='CompRegister'),  
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('<int:job_id>',HomeViews.ViewJob),  
    path('view/<int:job_id>',HomeViews.View),  
    path('Test',HomeViews.Test),
    path('MemberHome',HomeViews.MemberHome),

    path('Profile',CompViews.Profile, name='Update_Profile'),
    path('CreateJob',CompViews.Create_Job, name='CreateJob'),
    path('<int:job_id>/Edit',CompViews.edit_job),
    path('<int:job_id>/Update_Image_Job',CompViews.update_image_job),
    path('Update_Image',CompViews.update_image),
    path('<int:job_id>/Delete',CompViews.Delete_Job),
    path('Delete_Volunteer/<int:jobapply_id>/<int:Job_id>',CompViews.Delete_Volunteer),
    path('views/<int:job_id>',CompViews.View_Apply, name='รายชื่อผู้สมัคร'),
    path('myjob',CompViews.Myjob, name='Myjob'),
    path('ProfileApply/<int:member_id>',CompViews.ProfileApply,),


    path('apply/<int:job_id>',MemViews.Apply, name='apply'),
    path('CancelApply/<int:job_id>',MemViews.CancelApply, name='CancelApply'),
    path('ListApply',MemViews.ListApply, name='ListApply'),
    path('ProfileMember',MemViews.ProfileMember, name='ProfileMember'),

]
