from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required	

app_name = "foro"



urlpatterns = [
	#Busqueda 127.0.0.1:8000/foro
    url(r'^$', login_required(views.index), name='index'),

	#Posts de las sección de anuncios 127.0.0.1:8000/foro/anuncios
	url(r'^anuncios/$', login_required(views.anuncios), name='anuncios'),
	
	#Hilo 127.0.0.1:8000/foro/anuncios/hilo
	url(r'^anuncios/hilo/$', login_required(views.hilo), name='hilo'),

	#Mapa 127.0.0.1:8000/foro/mapa
	url(r'^mapa$', login_required(views.mapa), name='mapa'),

	#Acerca de... 127.0.0.1:8000/foro/acerca_de
	url(r'^acerca_de$', login_required(views.acerca_de), name='acerca_de')
]
