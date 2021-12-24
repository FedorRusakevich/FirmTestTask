from django_filters import rest_framework as filters
from .models import *


class EmployeesFilter(filters.FilterSet):
    level = filters.NumberFilter(field_name="level", lookup_expr='in')
    fields = ['level']