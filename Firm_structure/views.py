from rest_framework.views import APIView
from rest_framework_api_key.permissions import HasAPIKey
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .service import EmployeesFilter
from rest_framework import generics, permissions
from .tasks import add_salary

class AllEmployeesList(generics.ListAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesList
    filter_backends = (DjangoFilterBackend,)
    filterset_class = EmployeesFilter
    permission_classes = [permissions.IsAuthenticated]


class UserListView(APIView):
    permission_classes = (HasAPIKey,)


def add_slary(self, total_salary):
    total_salary.save()
    add_salary.delay(total_salary.instance)
    return super().add_slary(total_salary)

