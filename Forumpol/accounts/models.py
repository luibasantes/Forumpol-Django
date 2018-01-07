from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
def upload_location(instance,filename):
	return "profile_image/%s/%s" %(instance.id, filename)
	
	
class UserProfile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	city = models.CharField(max_length=25, default='')
	website = models.URLField(default='')
	phone = models.IntegerField(default=0)
	image = models.ImageField(upload_to= upload_location, blank=True)
	moderador = models.BooleanField(default=False)
	
	def __str__(self):
		return self.user.username

	
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)