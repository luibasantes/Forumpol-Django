"""Forumpol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.shortcuts import redirect
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.defaults import (permission_denied,
                                   page_not_found,
                                   server_error)

def redireccionarHome(request):
    return redirect('/foro/')
#from Foro.api.views import *
#from Foro.api.routers import HybridRouter
#router = HybridRouter()
#router.register(r'recursos', RecursoViewSet, r"recursos")

urlpatterns = [
    url(r'^$', redireccionarHome, name='index'),
    path('admin/', admin.site.urls),
	path(r'foro/', include('Foro.urls')),
	path(r'accounts/', include('accounts.urls')),
    path(r'api/', include('Foro.api.urls')),
    #path(r'mongoapi/',include(router.urls, namespace='api'))
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += [
        path(r'403/', permission_denied),
        path(r'404/', page_not_found),
        path(r'500/', server_error)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



