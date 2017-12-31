from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required	

app_name = "accounts"



urlpatterns = [
	#Busqueda 127.0.0.1:8000/accounts
    #url(r'^$', login_required(views.index), name='index'),
	
	
	#Busqueda 127.0.0.1:8000/accounts/profile
    url(r'^profile/$', login_required(views.view_profile), name='view_profile'),
	
	#Busqueda 127.0.0.1:8000/accounts/profile/edit_profile_basic_info
    url(r'^profile/edit_profile_basic_info/$', login_required(views.edit_profile_basic_info), name='edit_profile_basic_info'),

	#Busqueda 127.0.0.1:8000/accounts/profile/edit_profile_secondary_info
    url(r'^profile/edit_profile_secondary_info/$', login_required(views.edit_profile_secondary_info), name='edit_profile_secondary_info'),
	
	#Busqueda 127.0.0.1:8000/accounts/profile/change_password
    url(r'^profile/change_password/$', login_required(views.change_password), name='change_password'),
	
	#Busqueda 127.0.0.1:8000/accounts/register
	url(r'^register/$', views.register, name='register'),
	
	#Busqueda 127.0.0.1:8000/accounts/log
	url(r'^log_in/$', views.login_user, name='login_user'),
	
	#Busqueda 127.0.0.1:8000/accounts/log_out
	url(r'^log_out/$', views.logout_user, name='log_out'),


]
