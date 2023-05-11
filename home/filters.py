from dataclasses import field
import django_filters
from django_filters import CharFilter

from .models import Job

class JobFilter(django_filters.FilterSet):
    property = CharFilter(field_name='property', lookup_expr='icontains')
    category = CharFilter(field_name='category', lookup_expr='icontains')
    position = CharFilter(field_name='position', lookup_expr='icontains')
    compname = CharFilter(field_name='compname', lookup_expr='icontains')
    description = CharFilter(field_name='description', lookup_expr='icontains')
    type = CharFilter(field_name='type', lookup_expr='icontains')
    

    class Meta:
        model = Job
        fields = ['gpa']

