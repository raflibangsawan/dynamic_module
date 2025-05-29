# Dynamic Module System

A Django-based dynamic module system that allows for easy installation and management of modules. This system provides a flexible framework for adding and managing modules in your Django application. This application already deployed on https://web-production-ea3a.up.railway.app.

## Features

- Dynamic module installation and management
- Module registry and configuration
- User authentication and authorization
- Responsive UI with Tailwind CSS
- Easy module integration

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Node.js and npm (for Tailwind CSS)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd dynamic_module
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

4. Install Node.js dependencies and build Tailwind CSS:
```bash
npm install
npx tailwindcss -i ./static/css/main.css -o ./static/css/output.css --watch
```

5. Run database migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

## Running the Project

1. Start the development server:
```bash
python manage.py runserver
```

2. Open your browser and navigate to:
```
http://localhost:8000
```

## Project Structure

```
dynamic_module/
├── modules/
│   ├── your_module/          # Your custom module
│   │   ├── management/       # Management commands
│   │   ├── migrations/       # Database migrations
│   │   ├── templates/        # HTML templates
│   │   ├── models.py         # Database models
│   │   ├── views.py          # View logic
│   │   └── urls.py           # URL routing
│   └── main/                 # Core module system
├── static/
│   └── css/                  # CSS files
├── templates/                # Base templates
└── manage.py                 # Django management script
```

## Creating and Installing New Modules

### 1. Create Module Structure

Create a new directory under `modules/` with the following structure:
```
modules/your_module/
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── views.py
├── urls.py
├── mixins.py (optional)
└── templates/
    └── your_module/
        ├── list.html
        ├── form.html
        └── other_templates.html
```

### 2. Define Module Configuration

Create a `metadata.json` file in your module directory:
```json
{
    "name": "your_module",
    "display_name": "Your Module",
    "description": "Description of your module",
    "version": "1.0.0",
    "author": "Your Name",
    "dependencies": []
}
```

### 3. Create Module App Configuration

In `apps.py`:
```python
from django.apps import AppConfig

class YourModuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modules.your_module'
    verbose_name = 'Your Module'
```

### 4. Define Models

In `models.py`:
```python
from django.db import models

class YourModel(models.Model):
    # Define your model fields
    pass
```

### 5. Create Views

In `views.py`:
```python
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import YourModel
from .mixins import YourPermissionMixin

class YourListView(YourPermissionMixin, ListView):
    model = YourModel
    template_name = 'your_module/list.html'
```

### 6. Define URLs

In `urls.py`:
```python
from django.urls import path
from . import views

app_name = 'your_module'

urlpatterns = [
    path('', views.YourListView.as_view(), name='list'),
    path('create/', views.YourCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.YourUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.YourDeleteView.as_view(), name='delete'),
]
```

### 7. Add Module to Installed Apps

Add your module in settings.py INSTALLED_APPS
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tailwind',
    'theme',
    'main',
    'modules.<your_module>',
]
```

### 8. Create Migrations

```bash
python manage.py makemigrations your_module
python manage.py migrate
```


### 9. Access Module

Your module will be available at:
```
http://localhost:8000/your_module/
```
after installing via application

## Development

### Customizing Styles

1. Edit `static/css/main.css` for Tailwind CSS customizations
2. Run `npx tailwindcss -i ./static/css/main.css -o ./static/css/output.css --watch` to rebuild CSS

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 