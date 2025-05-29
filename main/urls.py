from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('modules/', views.home, name='home'),
    path('modules/<str:module_name>/install/', views.install_module, name='install_module'),
    path('modules/<str:module_name>/uninstall/', views.uninstall_module, name='uninstall_module'),
    path('modules/<str:module_name>/upgrade/', views.upgrade_module, name='upgrade_module'),
] 