from dataclasses import field
from django.forms import forms, ModelForm
from .models import Job, Image
from django import forms

class JobForm(ModelForm) :
    class Meta :
        model = Job
        fields = ['position','category','salary','quantity','type','logo','gpa','working_time','experience','description','property','welfare']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['name_Image', 'image']