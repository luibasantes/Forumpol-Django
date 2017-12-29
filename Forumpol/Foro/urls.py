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

]
