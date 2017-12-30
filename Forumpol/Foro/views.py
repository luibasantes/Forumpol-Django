from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login ,logout
from django.views import generic
from django.views.generic import View
from django.contrib.auth.models import User
from django.apps import apps

# Create your views here.
def index(request):
	username = request.user
	return render(request,"Foro/index.html",{'usuario':username})
		

def anuncios(request):
	username = request.user
	return render(request, "Foro/anuncios.html", {'usuario':username})
	
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