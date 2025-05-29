from django.shortcuts import render, redirect
from django.contrib import messages
from main.models import ModuleRegistry
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .module_manager import module_manager
from django.db import transaction
from main.url_manager import get_urlpatterns
import json
import os

def scan_modules():
    modules_dir = 'modules'
    new_modules = []
    for module_name in os.listdir(modules_dir):
        module_path = os.path.join(modules_dir, module_name)
        if os.path.isdir(module_path):
            metadata_path = os.path.join(module_path, 'metadata.json')
            if os.path.exists(metadata_path):
                with open(metadata_path, 'r') as f:
                    metadata = json.load(f)
                    module, created = ModuleRegistry.objects.get_or_create(
                        name=metadata['name'],
                        defaults={
                            'version': metadata['version'],
                            'metadata': metadata
                        }
                    )
                    if created:
                        new_modules.append(metadata['name'])
    return new_modules

@login_required
def home(request):
    new_modules = scan_modules()
    if new_modules:
        messages.info(request, f'New modules detected: {", ".join(new_modules)}')
    
    get_urlpatterns()
        
    modules = ModuleRegistry.objects.all().order_by('name')
    return render(request, 'main/module_list.html', {'modules': modules})

@login_required
def install_module(request, module_name):
    try:
        with transaction.atomic():
            module = ModuleRegistry.objects.select_for_update().get(name=module_name)
            module.is_installed = True
            module.save()
            
            module_app = f'modules.{module_name}'
            if module_app not in settings.INSTALLED_APPS:
                settings.INSTALLED_APPS.append(module_app)
            
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
