from django.contrib.auth.models import User
from .models import Post,Thread
from django import forms

"""
class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	
	
	class Meta:
		model = User
		fields = ['username','email','password']
"""

class CreateOriginalPostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = '__all__'
		exclude= ['date','owner','reply_to']

class CreateThreadForm(forms.ModelForm):

	class Meta:
		model = Thread
		fields = '__all__'
		exclude= ['op','category']