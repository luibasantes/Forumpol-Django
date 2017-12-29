from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login ,logout
from django.views import generic
from django.views.generic import View

# Create your views here.
def index(request):
	username = request.user
	return render(request,"index.html",{'usuario':username})
		

def anuncios(request):
	username = request.user
	return render(request, "anuncios.html", {'usuario':username})
	
def hilo(request):
	username = request.user
	return render(request,"hilo.html", {'usuario':username})

