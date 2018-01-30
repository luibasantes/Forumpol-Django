from django.db import models
from django.contrib.auth.models import User
from mongoengine import connect
from mongoengine import fields,Document,EmbeddedDocument
from bson import ObjectId
from mongoengine.base.datastructures import EmbeddedDocumentList
#connecting to mongo remote
connect(
    db='forumpol_db',
    username='jjcrow',
    password='forumpol2018',
    host='ds157667.mlab.com:57667',
    connect=False,
    maxPoolSize=1
)

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
	aprobado = models.NullBooleanField(default=None,null=True)

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
		return str(str(self.id) + " " + str(self.topic))\

class Archivo(EmbeddedDocument):
	_id = fields.ObjectIdField(default=ObjectId)
	nombre = fields.StringField(required=True)
	tamaño = fields.IntField(required=True)
	extension = fields.StringField(required=True)
	fichero = fields.FileField()


	@property
	def size_to_mb(self):
		return round((self.tamaño / 1048576),2)

	@property
	def id_to_str(self):
		return str(self._id)

class Recurso(Document):
	#_id = fields.ObjectIdField(required=True)
	titulo = fields.StringField(required=True)
	usuario = fields.IntField(required=True)
	nom_usuario= fields.StringField(required=True)
	categoria = fields.StringField(required=True)
	descripcion = fields.StringField(required=True)
	autor = fields.StringField(required=True)
	tags = fields.ListField(fields.StringField())
	fecha_creacion = fields.DateTimeField(required=True)
	is_active = fields.BooleanField(required=True)
	archivos = fields.EmbeddedDocumentListField(Archivo,required=True)

class Test(Document):
	title= fields.StringField(required=True)

class Club(models.Model):
	lat = models.DecimalField(null=False, default=0.0, max_digits=15, decimal_places=10)
	lng = models.DecimalField(null=False, default=0.0, max_digits=15, decimal_places=10)
	titulo = models.CharField(max_length=30, null=False, default='')

	def __str__(self):
		return self.titulo