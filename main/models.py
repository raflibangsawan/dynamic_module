from django.db import models

# Create your models here.

class ModuleRegistry(models.Model):
    name = models.CharField(max_length=100, unique=True)
    version = models.CharField(max_length=20)
    is_installed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    installed_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    metadata = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.name} (v{self.version})"
