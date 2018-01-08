from django.db import models
from django.contrib.auth.models import User
# Create your models here.

def upload_location(instance,filename):
	return "posted_images/%s/%s" %(instance.owner.id, filename)

class Post(models.Model):
	#RESPUESTA HACIA QUE POST (VACIO SI ES POST ORIGINAL
	reply_to = models.ForeignKey('self',blank=True, null=True,on_delete=models.SET_NULL)
	#Puede ser anuncio, Anuncio de CLUB , Vida Estudiantil
	content = models.TextField(max_length=500, default='')
	image = models.ImageField(upload_to=upload_location, blank=True,null=True)
	owner = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
	date = models.DateTimeField(auto_now=True)
	aprobado = models.BooleanField(default=False,null=False)

	def __str__(self):
		return str(str(self.id) + " " + str(self.owner))


class Thread(models.Model):
	#Original Post
	op = models.ForeignKey(Post,on_delete=models.CASCADE)
	#Puede ser anuncio, Anuncio de CLUB , Vida Estudiantil
	category = models.CharField(max_length=25, default='')
	topic = models.CharField(max_length=100, default='')
	respuestas = models.BigIntegerField(default=0)

	def __str__(self):
		return str(str(self.id) + " " + str(self.topic))
	
	