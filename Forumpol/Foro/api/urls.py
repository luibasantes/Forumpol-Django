from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import PostRudView, PostAPIView

urlpatterns = [
	#REST API
    # Leer, Actualizar, Borrar 127.0.0.1:8000/api/posts/Id_Post
    url(r'^(?P<pk>\d+)/$', login_required(PostRudView.as_view()), name='post_rud'),

    # Crear post 127.0.0.1:8000/api/posts
    url(r'^$', login_required(PostAPIView.as_view()), name='post_create'),
 ]