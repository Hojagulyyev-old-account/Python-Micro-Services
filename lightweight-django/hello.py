import os
import sys

from django.conf import settings

# settings.py
DEBUG = os.environ.get('DEBUG', 'on') == 'on'

SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

BASE_DIR = os.path.dirname(__file__)

settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
    ),
    TEMPLATES=(
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': (os.path.join(BASE_DIR, 'templates'), ),
        },
    ),
    STATICFILES_DIRS=(
        os.path.join(BASE_DIR, 'static'),
    ),
    STATIC_URL='/static/',
)

from django.urls import path, re_path
from django.core.wsgi import get_wsgi_application
from func_tools.django_css import django_css
from django.http import HttpResponse
from func_tools.clean_url import rpath, connect
from django.shortcuts import render

# views.py
def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def exone(request):
    return render(request, 'exercises/exercise-1.html', {})

# urls.py
urlpatterns = []

my_urlpatterns = [
    rpath(view=index),
    rpath('about/', about),
    rpath('exercise-1/', exone),
]

connect(urlpatterns, my_urlpatterns)

# manage.py
application = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
