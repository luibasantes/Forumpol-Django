from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import *
from ..api.routers import HybridRouter



urlpatterns = [
	#REST API
    # Leer, Actualizar, Borrar post 127.0.0.1:8000/api/posts/Id_Post
    url(r'^posts/(?P<pk>\d+)/$', PostRudView.as_view(), name='post_rud'),

    # Crear y Listar post 127.0.0.1:8000/api/posts
    url(r'^posts/$', PostAPIView.as_view(), name='post_create'),

    url(r'^posts/user/(?P<pk>\d+)/$', PostUserAPIView.as_view(), name='post_user'),

    # Leer, Actualizar, Borrar 127 thread 127.0.0.1:8000/api/threads/Id_Thread
    url(r'^threads/(?P<pk>\d+)/$', ThreadRudView.as_view(), name='thread_rud'),

    # Crear y Listar thread 127.0.0.1:8000/api/threads
    url(r'^threads/(?P<categoria>\w+)/$', ThreadAPIView.as_view(), name='thread_create'),

    #
	url(r'^recursos/$', RecursoViewSet.as_view({'get': 'list'}), name='recursos-view'),

	#
	url(r'^archivos/$', ArchivoViewSet.as_view({'get': 'list'}), name='archivos-view'),    
 ]