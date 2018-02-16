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
	url(r'^anuncios/crear/$', login_required(views.create_anuncio), name='create_anuncio'),

	#Aprobar post 127.0.0.1:8000/foro/anuncios/aprobar
	url(r'anuncios/aprobar/$', login_required(views.aprobar_post), name='aprobar_post'),

	#Aprobar post 127.0.0.1:8000/foro/anuncios/rechazados
	url(r'anuncios/rechazados/$', login_required(views.rechazar_post), name='rechazar_post'),

	#Aprobando post 127.0.0.1:8000/foro/anuncios/aprobar/#Post_ID/1 || 0
	url(r'anuncios/aprobar/(?P<Post_Id>[-]?[0-9]+)/(?P<value>(1|0))/$', login_required(views.aprobado), name='aprobado'),

	#Posts de las sección de anuncios 127.0.0.1:8000/foro/vida_estudiantil
	url(r'^vida_estudiantil/$', login_required(views.vida_estudiantil), name='vida_estudiantil'),

	#Posts de las sección de anuncios 127.0.0.1:8000/foro/anuncios/crear
	url(r'^vida_estudiantil/crear/$', login_required(views.create_experiencia), name='create_experiencia'),

	#Posts de las sección de anuncios 127.0.0.1:8000/foro/vida_estudiantil
	url(r'^clubs_espol/$', login_required(views.clubs_espol), name='clubs_espol'),

	#Posts de las sección de anuncios 127.0.0.1:8000/foro/anuncios/crear
	url(r'^clubs_espol/crear/$', login_required(views.create_evento_club), name='create_evento_club'),

	#Galeria 127.0.0.1:8000/foro/galeria
	url(r'^galeria/$', login_required(views.galeria), name='galeria'),

	#Mapa 127.0.0.1:8000/foro/mapa
	url(r'^mapa/$', login_required(views.mapa), name='mapa'),

	#Timeline 127.0.0.1:8000/foro/timeline
	url(r'^timeline/$', login_required(views.timeline), name='timeline'),

	#Acerca de... 127.0.0.1:8000/foro/acerca_de
	url(r'^acerca_de/$', login_required(views.acerca_de), name='acerca_de'),

	#Acerca de... 127.0.0.1:8000/foro/usuarios
	url(r'^usuarios/$', login_required(views.usuarios), name='usuarios'),

	#Aprobando post 127.0.0.1:8000/foro/anuncios/usuarios/banHammer/#user_id
	url(r'usuarios/banHammer/(?P<user_id>[-]?[0-9]+)/$', login_required(views.banHammer), name='banHammer'),

	#Aprobar post 127.0.0.1:8000/foro/panel_moderacion
	url(r'moderacion/$', login_required(views.moderacion), name='moderacion'),

	#Administrar posts 127.0.0.1:8000/foro/administrar_posts
	url(r'administrar_posts/$', login_required(views.admin_posts), name='admin_posts'),

	#Administrar posts 127.0.0.1:8000/foro/adminstrar_posts/buscar
	url(r'administrar_posts/buscar$', login_required(views.buscar), name='buscar'),

	#Repositorio localhost:8000/foro/repositorio
	url(r'repositorio/$',login_required(views.repo),name='repo'),

	url(r'repositorio/tags/(?P<tag_name>([a-zA-Z]|[0-9]| )+)/$',login_required(views.recursos_por_tag),name="recursos_tags"),

	url(r'repositorio/user/(?P<user_id>([0-9])+)/$',login_required(views.mis_recursos),name="mis_recursos"),

	url(r'repositorio/(?P<recurso_id>([a-zA-Z]|[0-9])+)/$',login_required(views.informacion_recurso),name="info_recurso"),

	url(r'repositorio/(?P<recurso_id>([a-zA-Z]|[0-9])+)/file/(?P<archivo_id>([a-zA-Z]|[0-9])+)/$',login_required(views.descargar_archivo),name="descarga_archivo"),
	
	url(r'repositorio/agregar_recurso$',login_required(views.agregar_recurso),name="agregar_recurso"),

	url(r'repositorio/user/(?P<user_id>([0-9])+)/edit/(?P<recurso_id>([a-zA-Z]|[0-9])+)/$',login_required(views.editar_recurso),name="editar_recurso"),

	url(r'folletos/$',login_required(views.folletos),name='folletos'),

	url(r'folletos/(?P<recurso_id>([a-zA-Z]|[0-9])+)/$',login_required(views.informacion_folleto),name="info_folleto"),

	url(r'folletos/agregar_folleto$',login_required(views.agregar_folleto),name="agregar_folleto"),

	url(r'folletos/user/(?P<user_id>([0-9])+)/$',login_required(views.mis_folletos),name="mis_folletos"),

	url(r'folletos/tags/(?P<tag_name>([a-zA-Z]|[0-9]| )+)/$',login_required(views.folletos_por_tag),name="folletos_tags"),
]