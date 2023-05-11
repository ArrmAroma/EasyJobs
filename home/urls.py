from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('', views.Home),
    # path('FindJob',views.FindJob, name='findjob'),
    # path('login',views.Login, name='login'),
    # path('MemberRegister',views.MemberRegister, name='register'),
    # path('CompRegister',views.CompRegister, name='CompRegister'),
    # path('CreateJob',views.Create_Job, name='CreateJob'),
    # path('myjob',views.Myjob, name='Myjob'),
    # # path('/index', Index),    .
    # path('logout', auth_views.LogoutView.as_view(), name='logout'),
    # # path('ViewJob', views.ViewJob),
    # path('<int:job_id>/Edit',views.edit_job),
    # path('<int:job_id>/Delete',views.Delete_Job),
    # path('<int:job_id>',views.ViewJob),
    # path('view/<int:job_id>',views.View_Apply),
    # path('Profile',views.Profile),
    # path('Test',views.Test),
]