from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login ,logout
from django.views import generic
from django.views.generic import View

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

