from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import password_reset , password_reset_done, password_reset_confirm, password_reset_complete

app_name = "accounts"



urlpatterns = [
	#Busqueda 127.0.0.1:8000/accounts
    #url(r'^$', login_required(views.index), name='index'),
	
	#Fue actualizado por el siguiente
	#Busqueda 127.0.0.1:8000/accounts/profile
    #url(r'^profile/$', login_required(views.view_profile), name='view_profile'),
	
	#Busqueda 127.0.0.1:8000/accounts/profile/user_id
    url(r'^profile/(?P<user_id>[0-9]+)/$', login_required(views.view_profile), name='view_profile'),
	
	#Busqueda 127.0.0.1:8000/accounts/profile/edit
    url(r'^profile/edit_profile/$', login_required(views.edit_profile), name='edit_profile'),
	
	#Busqueda 127.0.0.1:8000/accounts/profile/change_password
    url(r'^profile/change_password/$', login_required(views.change_password), name='change_password'),

    #Busqueda 127.0.0.1:8000/accounts/reset_password
    url(r'^reset_password/$', password_reset,{'template_name':'Accounts/reset_password.html','post_reset_redirect':'accounts:password_reset_done', 'email_template_name': 'Accounts/reset_password_email.html'},name='reset_password'),

    #Busqueda 127.0.0.1:8000/accounts/reset_password/done
    url(r'^reset_password/done/$', password_reset_done,{'template_name':'Accounts/reset_password_done.html'}, name='password_reset_done'),

    #Busqueda 127.0.0.1:8000/accounts/reset_password/confirm
    url(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'post_reset_redirect': 'accounts:password_reset_complete'},name='password_reset_confirm'),

    #Busqueda 127.0.0.1:8000/accounts/reset_password/complete
    url(r'^reset_password/complete/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_complete, name='password_reset_complete'),
	
	#Busqueda 127.0.0.1:8000/accounts/register
	url(r'^register/$', views.register, name='register'),
	
	#Busqueda 127.0.0.1:8000/accounts/log
	url(r'^log_in/$', views.login_user, name='login_user'),
	
	#Busqueda 127.0.0.1:8000/accounts/log_out
	url(r'^log_out/$', views.logout_user, name='log_out'),


]
