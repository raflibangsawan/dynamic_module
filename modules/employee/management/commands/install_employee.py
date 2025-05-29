from django.core.management.base import BaseCommand
from main.models import ModuleRegistry
import json
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Install the employee module'

    def handle(self, *args, **options):
        try:
            metadata_path = os.path.join(settings.BASE_DIR, 'modules', 'employee', 'metadata.json')
            with open(metadata_path, 'r') as f:
                metadata = json.load(f)

            module, created = ModuleRegistry.objects.get_or_create(
                name=metadata['name'],
                defaults={
                    'version': metadata['version'],
                    'is_installed': True,
                    'is_active': True,
                    'metadata': metadata
                }
            )

            if not created:
                module.version = metadata['version']
                module.is_installed = True
                module.is_active = True
                module.metadata = metadata
                module.save()

            self.stdout.write(self.style.SUCCESS(f'Successfully installed employee module v{metadata["version"]}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error installing employee module: {str(e)}')) 