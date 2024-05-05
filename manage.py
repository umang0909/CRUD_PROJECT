#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

sys.path.append('/Users/umangshah/Desktop/crud_project/venv/lib/python3.9/site-packages')
import django

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crud_project.settings')
    django.setup()
    # Check if Django is available on PYTHONPATH

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    



if __name__ == '__main__':
    main()

"""
Commands to use:
django-admin startproject crud_project
cd crud_project
python manage.py startapp employee
pip install django-cors-headers
python -m django --version
pip show django | grep Location
pip show django
pip uninstall django
pip install django
python3 -m venv myenv
source myenv/bin/activate
pip install django
python manage.py makemigrations employee
python manage.py migrate
python manage.py runserver
python manage.py shell
"""