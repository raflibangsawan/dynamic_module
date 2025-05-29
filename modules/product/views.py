from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from main.models import ModuleRegistry
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import ProductPermissionMixin

# Create your views here.

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})

class ProductListView(LoginRequiredMixin, ProductPermissionMixin, ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()

class ProductCreateView(LoginRequiredMixin, ProductPermissionMixin, CreateView):
    model = Product
    template_name = 'product/product_form.html'
    fields = ['name', 'barcode', 'price', 'stock']
    success_url = reverse_lazy('product:product_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, ProductPermissionMixin, UpdateView):
    model = Product
    template_name = 'product/product_form.html'
    fields = ['name', 'barcode', 'price', 'stock']
    success_url = reverse_lazy('product:product_list')

class ProductDeleteView(LoginRequiredMixin, ProductPermissionMixin, DeleteView):
    model = Product
    template_name = 'product/product_confirm_delete.html'
    success_url = reverse_lazy('product:product_list')
