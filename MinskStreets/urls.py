"""MinskStreets URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import ListView, DetailView, TemplateView

from main.models import StreetModel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListView.as_view(model=StreetModel, template_name='index.html'), name='index'),
    path('streets/', ListView.as_view(model=StreetModel, template_name='streetsList.html'), name='streets'),
    path('about/', TemplateView.as_view(template_name='about.html'), name="about"),
    path('streets/<slug:slug>', DetailView.as_view(model=StreetModel, template_name='street.html'), name='street_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
