from rest_framework import viewsets, permissions

from api.models import Organization, Department, Employees
from api.serializers import OrganizationSerializer, DepartmentSerializer, EmployeesSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    http_method_names = ['get']
    permission_classes = (permissions.IsAuthenticated,)


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    http_method_names = ['get']


class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    http_method_names = ['get']



def count_call_endpoint():
    request_count = 0
    return request_count


def request_time():
    request_time = 0
    return request_time
