from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse
from django.http import Http404,HttpResponseForbidden
from django.contrib.auth.models import User

from .forms import UserForm, EditProfileForm, EditUserForm


# Create your views here.


#Esta quedo desactualizado
'''

def view_profile(request):
	context = {'user':request.user,'usuario':request.user.username}
	return render(request, 'Accounts/profile.html',context)
'''	
def view_profile(request,user_id):
	user = request.user
	if not (user.id == int(user_id) or user.is_staff or user.userprofile.moderador):
		return HttpResponseForbidden()
	try:
		usuario = User.objects.get(id = str(user_id))
	except User.DoesNotExist:
		raise Http404("Usuario No existe")
	
	context = {'user':user,'usuarioPerfil':usuario}
	return render(request, 'Accounts/profile.html',context)
	
	
	
'''
def edit_profile_basic_info(request):
	if request.method == 'POST':
		user_form = EditUserForm(request.POST, instance=request.user)
		if user_form.is_valid():
			user_form.save()
			return redirect(reverse('accounts:view_profile'))
	else:
		user_form = EditUserForm(instance=request.user)
		context = {'user_form': user_form,'usuario':request.user}
		return render(request, 'Accounts/edit_profile.html', context)

def edit_profile_secondary_info(request):
	if request.method == 'POST':
		profile_form = EditProfileForm(request.POST, instance=request.user.userprofile)
		if profile_form.is_valid():
			profile_form.save()
			return redirect(reverse('accounts:view_profile'))
	else:
		profile_form = EditProfileForm(instance=request.user.userprofile)
		context = {'profile_form': profile_form,'usuario':request.user}
		return render(request, 'Accounts/edit_profile.html', context)
'''
	

def edit_profile(request):
	if request.method == 'POST':
		user_form = EditUserForm(request.POST, instance=request.user,prefix="form1")
		profile_form = EditProfileForm(request.POST,request.FILES or None, instance=request.user.userprofile,prefix="form2")
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			return redirect('accounts:view_profile',user_id =request.user.id)
	else:
		user_form = EditUserForm(instance=request.user,prefix="form1")
		profile_form = EditProfileForm(instance=request.user.userprofile,prefix="form2")
		context = {'user_form': user_form, 'profile_form': profile_form,'usuario':request.user}
		return render(request, 'Accounts/edit_profile.html', context)

def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect(reverse('accounts:view_profile'))
		else:
			return redirect(reverse('accounts:change_password'))
	else:
		form = PasswordChangeForm(user=request.user)

		context = {'user_form': form,'usuario':request.user.username}
		return render(request,'Accounts/change_password.html', context)
	
def login_user(request):
	logout(request)
	if request.method == "POST":
		try:
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return render(request,'Foro/index.html', {'usuario':username})
				else:
					return render(request, 'Accounts/login_user.html', {'error_message': 'Your account has been disabled'})
			else:
				return render(request, 'Accounts/login_user.html', {'error_message': 'Invalid login'})
		except:
			print("Algo paso al cargar el login_user.")
	return render(request, 'Accounts/login_user.html')

		
def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {"form": form}
    return render(request, 'accounts/login_user.html', context)
	
def register(request):
	logout(request)
	form = UserForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		first_name = form.cleaned_data['first_name']
		last_name = form.cleaned_data['last_name']
		user.set_password(password)
		user.save()
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('/foro')
	context = {"form": form,}
	return render(request, 'accounts/register.html', context)
	
	
	
	
	
	
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