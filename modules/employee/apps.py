from django.apps import AppConfig

class EmployeeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modules.employee'
    verbose_name = 'Employee Management'
