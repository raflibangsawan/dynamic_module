import json
import os
from django.core.management.base import BaseCommand
from main.models import ModuleRegistry

class Command(BaseCommand):
    help = 'Scans the modules directory and updates the module registry.'

    def handle(self, *args, **options):
        modules_dir = 'modules'
        for module_name in os.listdir(modules_dir):
            module_path = os.path.join(modules_dir, module_name)
            if os.path.isdir(module_path):
                metadata_path = os.path.join(module_path, 'metadata.json')
                if os.path.exists(metadata_path):
                    with open(metadata_path, 'r') as f:
                        metadata = json.load(f)
                        ModuleRegistry.objects.update_or_create(
                            name=metadata['name'],
                            defaults={
                                'version': metadata['version'],
                                'metadata': metadata
                            }
                        )
                        self.stdout.write(self.style.SUCCESS(f'Module {metadata["name"]} updated.')) 