from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

def get_urlpatterns():
    """Get all URL patterns."""
    from .models import ModuleRegistry
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')),
        path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    ]

    for module in ModuleRegistry.objects.all():
        try:
            urlpatterns.append(
                path(f'{module.name}/', include(f'modules.{module.name}.urls'))
            )
        except Exception as e:
            print(f"Error including URLs for module {module.name}: {str(e)}")
    
    return urlpatterns 