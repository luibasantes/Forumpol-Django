from .models import Post,Thread,Fecha
from django import forms

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


class CreateFechaForm(forms.ModelForm):
	class Meta:
		model = Fecha
		fields = '__all__'
		widgets = {
			'desc': forms.Textarea(attrs={'cols': 80, 'rows': 7})
		}