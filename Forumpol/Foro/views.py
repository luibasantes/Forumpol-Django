from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login ,logout
from django.views import generic
from django.views.generic import View
from django.contrib.auth.models import User
from django.apps import apps
from .forms import CreateOriginalPostForm, CreateThreadForm
from .models import Post,Thread
from django.urls import reverse
from django.http import Http404

# Create your views here.
def index(request):

	username = request.user
	return render(request,"Foro/index.html",{'usuario':username})
		

def anuncios(request):
	all_anuncios = Thread.objects.filter(category="anuncio")
	username = request.user
	context = {'usuario':username,"anuncios":all_anuncios}
	return render(request, "Foro/anuncios.html", context)
	
#Vista detallada de cada Post
def detalle_anuncio(request,Post_Id):
	try:
		post = Post.objects.get(id = str(Post_Id))
		thread = Thread.objects.get(op=post)
		contenido = contenido={"anuncio":post,'thread':thread}
		
	except Post.DoesNotExist:
		raise Http404("Anuncio no existe")
	return render(request,"foro/anuncio.html",contenido)
	
	
def create_anuncio(request):
	
	form_Thread = CreateThreadForm(request.POST or None)
	form_Post = CreateOriginalPostForm(request.POST or None)
	if form_Thread.is_valid() and form_Post.is_valid():
		my_Post = form_Post.save(commit=False)
		my_Post.owner = request.user
		my_Post.save()
		
		my_thread = form_Thread.save(commit=False)
		my_thread.category ='anuncio'
		my_thread.op =Post.objects.last()
		my_thread.save()
		return redirect(reverse('foro:anuncios'))
	context = {'user_form': form_Thread, 'profile_form': form_Post,'usuario':request.user}
	return render(request, 'Foro/create_anuncio.html', context)


	
def hilo(request):
	username = request.user
	return render(request,"Foro/hilo.html", {'usuario':username})

def mapa(request):
	username = request.user
	return render(request, "Foro/mapa.html", {'usuario':username})

def acerca_de(request):
	admins = []
	username = request.user
	staff = User.objects.filter(is_staff=True)
	return render(request, "Foro/acercaDe.html", {'usuario':username, 'staff':staff})