from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login ,logout
from django.views import generic
from django.views.generic import View
from .forms import UserForm

# Create your views here.
def index(request):
	return render(request,"index.html")
		
	
def login_user(request):
	logout(request)
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return render(request,'index.html', {})
			else:
				return render(request, 'login_user.html', {'error_message': 'Your account has been disabled'})
		else:
			return render(request, 'login_user.html', {'error_message': 'Invalid login'})
	return render(request, 'login_user.html')

		
def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {"form": form,}
    return render(request, 'login_user.html', context)
	
def register(request):
	form = UserForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user.set_password(password)
		user.save()
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return render(request, 'index.html', {})
	context = {"form": form,}
	return render(request, 'register.html', context)
	
	
	
"""	
class UserFormView(View):
	form_class = UserForm
	template_name = "registration_form.html"
	
	
	#Display Blank Form 
	def get(self,request):
		form = self.form_class(None)
		return render(request,self.template_name,{'form':form})
		
	#Process Form Data
	def post(self,request):
		form = self.form_class(request.POST)
		
		if form.is_valid():
			user = 	form.save(commit="False")
			
			#Cleaned (normalized) Data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			#Cambiar contraseña   user.set_password() 
			user.set_password(password)
			user.save()			
			
			
			#Validar el login	
			#returns User Objects if credentials are correct
			user = authenticate(username=username,password=password)
			if user is not None:
				if user.is_active:
					login(request,user)
					return redirect("foro:index")
		return render(request,self.template_name,{'form':form})"""