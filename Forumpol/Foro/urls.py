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
	
	#Posts de las sección de anuncios 127.0.0.1:8000/foro/anuncios/#IdDePost
	url(r'^anuncios/(?P<Post_Id>[-]?[0-9]+)/$', login_required(views.detalle_anuncio), name='detalle_anuncio'),
	
	#Posts de las sección de anuncios 127.0.0.1:8000/foro/anuncios/crear
	url(r'^anuncios/crear$', login_required(views.create_anuncio), name='create_anuncio'),

	#Galeria 127.0.0.1:8000/foro/galeria
	url(r'^galeria$', login_required(views.galeria), name='galeria'),

	#Mapa 127.0.0.1:8000/foro/mapa
	url(r'^mapa$', login_required(views.mapa), name='mapa'),

	#Timeline 127.0.0.1:8000/foro/timeline
	url(r'^timeline$', login_required(views.timeline), name='timeline'),

	#Acerca de... 127.0.0.1:8000/foro/acerca_de
	url(r'^acerca_de$', login_required(views.acerca_de), name='acerca_de'),

	#Aprobar post 127.0.0.1:8000/foro/anuncios/aprobar
	url(r'anuncios/aprobar$', login_required(views.aprobar), name='aprobar'),

	#Aprobando post 127.0.0.1:8000/foro/anuncios/aprobar/Post_ID
	url(r'anuncios/aprobar/(?P<Post_Id>[-]?[0-9]+)/$', login_required(views.aprobado), name='aprobado'),
]
