from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
	#REST API
    # Leer, Actualizar, Borrar post 127.0.0.1:8000/api/posts/Id_Post
    url(r'^posts/(?P<pk>\d+)/$', PostRudView.as_view(), name='post_rud'),

    # Crear y Listar post 127.0.0.1:8000/api/posts
    url(r'^posts/$', PostAPIView.as_view(), name='post_create'),

    # Leer, Actualizar, Borrar 127 thread 127.0.0.1:8000/api/threads/Id_Thread
    url(r'^threads/(?P<pk>\d+)/$', ThreadRudView.as_view(), name='thread_rud'),

    # Crear y Listar thread 127.0.0.1:8000/api/threads
    url(r'^threads/$', ThreadAPIView.as_view(), name='thread_create'),
 ]