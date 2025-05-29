from django.shortcuts import redirect
from django.contrib import messages
from .models import ModuleRegistry
from django.urls import resolve, Resolver404

class ModuleAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path.strip('/')
        
        module_name = path.split('/')[0] if path else None
        
        if module_name in ['admin', 'login', 'logout', '']:
            return self.get_response(request)
        
        if module_name:
            try:
                module = ModuleRegistry.objects.get(name=module_name)
                if not module.is_installed:
                    messages.error(request, f'Module {module_name} is not installed.')
                    return redirect('home')
            except ModuleRegistry.DoesNotExist:
                pass
        
        response = self.get_response(request)
        return response 