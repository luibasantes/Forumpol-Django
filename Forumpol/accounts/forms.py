from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import UserChangeForm
from django import forms

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
		
		
class EditProfileForm(UserChangeForm):
    template_name='/something/else'

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )
