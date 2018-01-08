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
		widgets = {
			'content': forms.Textarea(attrs={'cols': 80, 'rows': 7}),
		}
		exclude= ['date','owner','reply_to','aprobado']

class CreateThreadForm(forms.ModelForm):

	class Meta:
		model = Thread
		fields = '__all__'
		exclude= ['op','category','respuestas']