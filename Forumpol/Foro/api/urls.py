from django.conf.urls import url
#from django.contrib.auth.decorators import login_required
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
    url(r'^threads/all/$', Thread_stats.as_view(), name='thread_all'),

    # Crear y Listar thread 127.0.0.1:8000/api/threads
    url(r'^threads/(?P<categoria>\w+)/$', ThreadAPIView.as_view(), name='thread_create'),

    # Listar recursos 127.0.0.1:8000/api/recursos
	url(r'^recursos/$', RecursoViewSet.as_view({'get': 'list'}), name='recursos-view'),

	#Listar recursos por  usuario
	url(r'^recursos/(?P<pk>\d+)/$', RecursoViewSet.as_view({'get': 'retrieve'}), name='recursos-user'),

	#Listar recursos por  tag
	url(r'^recursos/(?P<pk>([a-zA-Z]|\d| )+)/$', RecursoViewSet.as_view({'get': 'retrieve'}), name='recursos-tags'),

	#Listar resumen de tags
	url(r'^recursos/tags_count/$', RecursoViewSet.as_view({'get': 'showFiles'}), name='resumen-tags'),

	#Modificar un recurso
	url(r'^recursos/edit/(?P<pk>([a-zA-Z]|\d)+)/$', RecursoViewSet.as_view({'put': 'partial_update'}), name='recursos-edit'),
	#
	url(r'^archivos/$', ArchivoViewSet.as_view({'get': 'list'}), name='archivos-view'),

	# Listar los usuarios con la cantidad de post 127.0.0.1:8000/api/users_stats
	url(r'^users_stats/$', User_stats.as_view(), name='users_stats'),

	url(r'^users_stats/(?P<pk>([a-zA-Z]|\d)+)/$', User_stats_by_id.as_view(), name='users_stats'),

    #Listar los clubes
    url(r'^clubs/$', ClubAPIView.as_view(), name='club_list'),
 ]