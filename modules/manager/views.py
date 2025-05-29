from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Manager

class ManagerListView(LoginRequiredMixin, ListView):
    model = Manager
    template_name = 'manager/manager_list.html'
    context_object_name = 'managers'
