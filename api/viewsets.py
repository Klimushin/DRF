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


count = 0
request_time = []


def count_call_endpoint():
    global count
    count += 1
    request_count = count
    print(request_count)
    return request_count


def average_request_time(total_time):
    global request_time
    request_time.append(total_time)
    average_time = sum(request_time) / len(request_time)
    print(average_time)
    return average_time
