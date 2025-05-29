from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('', views.payment_list, name='payment_list'),
    path('create/', views.payment_create, name='payment_create'),
    path('<int:pk>/delete/', views.payment_delete, name='payment_delete'),
] 