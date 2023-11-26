"""
URL configuration for AccountingWorld project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from silk import urls as silk_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('AccountingWorld.apps.users.urls')),
    path('dashboard/', include('AccountingWorld.apps.dashboard.urls')),
    path('silk/', include(silk_urls, namespace='silk')),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

# 'staticfiles_urlpatterns' function is part of the Django Framework and is used to serve
# static files during development. It is typically added to the 'urlpatterns' in Django project's urls.py

# staticfiles_urlpatterns() function is added to the 'urlpatterns' list. This is useful during development because
# Django development server can serve static files directly. Note that this approach is not suitable for production;
# In a production environment , you should configure your web server (e.g; Nginix or Apache) to serve static files

# 'staticfiles_urlpatterns' function is only intended for use during development and Django will
# handle static files differently in production
