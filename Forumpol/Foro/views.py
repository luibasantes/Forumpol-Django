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
	all_anuncios = Thread.objects.filter(category="anuncio").order_by("-id")
	username = request.user
	context = {'usuario':username,"anuncios":all_anuncios}
	return render(request, "Foro/anuncios.html", context)
	
#Vista detallada de cada Post
def detalle_anuncio(request,Post_Id):
	form_Post = CreateOriginalPostForm(request.POST or None,request.FILES or None)
	try:
		post = Post.objects.get(id = str(Post_Id))
		thread = Thread.objects.get(op=post)
		respuestas = Post.objects.filter(reply_to = str(Post_Id))
	except Post.DoesNotExist:
		raise Http404("Anuncio no existe")
	except Thread.DoesNotExist:
		raise Http404("Anuncio no es OP	")
		
	if 	form_Post.is_valid():
		my_Post = form_Post.save(commit=False)
		my_Post.reply_to = Post.objects.get(id = str(Post_Id))
		my_Post.owner = request.user
		my_Post.save()
		thread.respuestas += 1
		thread.save()
		form_Post = CreateOriginalPostForm(request.POST or None,request.FILES or None)
		contenido={"anuncio":post,'thread':thread,'usuario':request.user,'respuestas':respuestas,'form':form_Post}	
		return render(request,"foro/hilo.html",contenido)
	contenido={"anuncio":post,'thread':thread,'usuario':request.user,'respuestas':respuestas,'form':form_Post}	
	return render(request,"foro/hilo.html",contenido)
	
	
def create_anuncio(request):
	form_Thread = CreateThreadForm(request.POST or None)
	form_Post = CreateOriginalPostForm(request.POST or None,request.FILES or None)
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

def galeria(request):
	username = request.user
	info = dict()
	posts = Post.objects.all()
	for post in posts:
		if post.image:
			if post.reply_to:
				info[post] = Thread.objects.get(op=post.reply_to)
			else:
				info[post] = Thread.objects.get(op=post)
	return render(request,"Foro/galeria.html", {'usuario':username, 'info':info})
	
def hilo(request):
	username = request.user
	return render(request,"Foro/hilo.html", {'usuario':username})

def mapa(request):
	username = request.user
	return render(request, "Foro/mapa.html", {'usuario':username})

def timeline(request):
	username = request.user
	return render(request, "Foro/fechas.html", {'usuario': username})

def acerca_de(request):
	admins = []
	username = request.user
	staff = User.objects.filter(is_staff=True)
	return render(request, "Foro/acercaDe.html", {'usuario':username, 'staff':staff})