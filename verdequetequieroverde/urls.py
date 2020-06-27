"""verdequetequieroverde URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views

admin.site.site_header = 'Verde Que Te Quiero Verde - Voluntarios'
admin.site.site_title = 'Voluntarios'
admin.site.index_title = 'Verde Que Te Quiero Verde administration'
admin.empty_value_display = '**Empty**'

urlpatterns = [
    path("", views.home, name="home"),
    path('events/', include('events.urls')),
    path('admin/', admin.site.urls),
    path('prizes/', include('prizes.urls')),
    path('materials/', include('materials.urls')),
    path('workgroups/', include('workgroups.urls')),
    path('trivias/', include('trivias.urls')),
]
