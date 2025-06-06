import json
import os
from django.conf import settings
from django.core.management import call_command
from .models import ModuleRegistry
from django.db import transaction

class ModuleManager:
    @staticmethod
    def update_module_metadata(module_name):
        """Update module metadata from metadata.json file."""
        try:
            module_path = os.path.join(settings.BASE_DIR, 'modules', module_name)
            metadata_path = os.path.join(module_path, 'metadata.json')
            
            if not os.path.exists(metadata_path):
                raise FileNotFoundError(f"metadata.json not found for module {module_name}")
            
            with open(metadata_path, 'r') as f:
                metadata = json.load(f)
            
            with transaction.atomic():
                module = ModuleRegistry.objects.select_for_update().get(name=module_name)
                module.version = metadata['version']
                module.metadata = metadata
                module.save()
            
            return True
        except Exception as e:
            print(f"Error updating module metadata: {str(e)}")
            return False
    
    @staticmethod
    def run_module_migrations(module_name):
        """Run migrations for a specific module."""
        try:
            if settings.DEBUG:
                call_command('makemigrations', module_name)
            
            call_command('migrate', module_name)
            return True
        except Exception as e:
            print(f"Error running migrations: {str(e)}")
            return False
    
    @staticmethod
    def upgrade_module(module_name):
        """Upgrade a module by updating metadata and running migrations."""
        try:
            module = ModuleRegistry.objects.get(name=module_name)
            if not module.is_installed:
                raise ValueError(f"Module {module_name} is not installed")
            
            if not ModuleManager.update_module_metadata(module_name):
                return False
            
            if not ModuleManager.run_module_migrations(module_name):
                return False
            
            return True
        except ModuleRegistry.DoesNotExist:
            print(f"Module {module_name} not found")
            return False
        except Exception as e:
            print(f"Error upgrading module: {str(e)}")
            return False

module_manager = ModuleManager() 