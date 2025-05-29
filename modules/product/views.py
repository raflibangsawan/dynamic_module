from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from main.models import ModuleRegistry
from django.contrib import messages

def check_module_installed(view_func):
    def wrapper(request, *args, **kwargs):
        try:
            module = ModuleRegistry.objects.get(name='product')
            if not module.is_installed:
                messages.error(request, 'Product module is not installed.')
                return redirect('home')
            return view_func(request, *args, **kwargs)
        except ModuleRegistry.DoesNotExist:
            messages.error(request, 'Product module not found.')
            return redirect('home')
    return wrapper

# Create your views here.

@login_required
@check_module_installed
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})
