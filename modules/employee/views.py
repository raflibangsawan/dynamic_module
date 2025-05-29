from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Employee

class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee/employee_list.html'
    context_object_name = 'employees'
