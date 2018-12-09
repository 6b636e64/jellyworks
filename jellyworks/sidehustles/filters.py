from .models import Services
from django import forms
import django_filters

class UserFilter(django_filters.FilterSet):
    public_displayname = django_filters.CharFilter(lookup_expr='icontains')
    service_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Services
        fields = ['public_displayname', 'service_name', 'skill', 'location', 'availability']
