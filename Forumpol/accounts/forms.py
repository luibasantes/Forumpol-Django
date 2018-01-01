from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django import forms
from .models import UserProfile

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	email = forms.EmailField(required=True)
	
	class Meta:
		model = User
		fields = ['username',
		'first_name',
		'last_name',
		'email',
		'password'
		]

class EditUserForm(UserChangeForm):
	class Meta:
		model = User
		fields = ['first_name',
				  'last_name',
				  'email',
				  'password'
				  ]

class EditProfileForm(forms.ModelForm):

	class Meta:
		model = UserProfile
		fields = '__all__'
		exclude= ['user']
