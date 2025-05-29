from django.shortcuts import render, redirect
from django.contrib import messages
from main.models import ModuleRegistry
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .module_manager import module_manager
from django.db import transaction

# Create your views here.

@login_required
def home(request):
    modules = ModuleRegistry.objects.all()
    return render(request, 'main/module_list.html', {'modules': modules})

@login_required
def install_module(request, module_name):
    try:
        with transaction.atomic():
            module = ModuleRegistry.objects.select_for_update().get(name=module_name)
            module.is_installed = True
            module.save()
            
            # Add module to INSTALLED_APPS if not already present
            module_app = f'modules.{module_name}'
            if module_app not in settings.INSTALLED_APPS:
                settings.INSTALLED_APPS.append(module_app)
            
            # Run migrations after installation
            if not module_manager.run_module_migrations(module_name):
                raise Exception("Failed to run module migrations")
            
            messages.success(request, f'Module {module_name} installed successfully.')
    except ModuleRegistry.DoesNotExist:
        messages.error(request, f'Module {module_name} not found.')
    except Exception as e:
        messages.error(request, f'Error installing module: {str(e)}')
    
    return redirect('home')

@login_required
def uninstall_module(request, module_name):
    try:
        with transaction.atomic():
            module = ModuleRegistry.objects.select_for_update().get(name=module_name)
            module.is_installed = False
            module.save()
            
            # Remove module from INSTALLED_APPS if present
            module_app = f'modules.{module_name}'
            if module_app in settings.INSTALLED_APPS:
                settings.INSTALLED_APPS.remove(module_app)
            
            messages.success(request, f'Module {module_name} uninstalled successfully.')
    except ModuleRegistry.DoesNotExist:
        messages.error(request, f'Module {module_name} not found.')
    except Exception as e:
        messages.error(request, f'Error uninstalling module: {str(e)}')
    
    return redirect('home')

@login_required
def upgrade_module(request, module_name):
    try:
        with transaction.atomic():
            module = ModuleRegistry.objects.select_for_update().get(name=module_name)
            if not module.is_installed:
                messages.error(request, f"Module {module_name} is not installed")
                return redirect('home')
            
            if module_manager.upgrade_module(module_name):
                messages.success(request, f"Module {module_name} upgraded successfully")
            else:
                messages.error(request, f"Failed to upgrade module {module_name}")
    except ModuleRegistry.DoesNotExist:
        messages.error(request, f"Module {module_name} not found")
    except Exception as e:
        messages.error(request, f"Error upgrading module: {str(e)}")
    
    return redirect('home')
