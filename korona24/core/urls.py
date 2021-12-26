"""korona24 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import (
    path,
    include,
)

from services.views import prices

urlpatterns = [
    path('', include('main.urls')),
    path('eto-interesno/', include('blog.urls')),
    path('testimonials/', include('comments.urls')),
    path('uslugi/', include('services.urls')),
    path('cena/', prices, name='prices'),
    path('about/vrachi-sk-korona/', include('employees.urls')),
    path('about/', include('pages.urls')),
    path('foto-i-video/', include('gallery.urls')),
    path('visual-version/', include('visual_version_handler.urls')),
    path('admin/', admin.site.urls),
    url(r'mdeditor/', include('mdeditor.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
