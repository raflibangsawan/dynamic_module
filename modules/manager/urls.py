from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [
    path('', views.ManagerListView.as_view(), name='manager_list'),
]
