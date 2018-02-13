from django.contrib import admin
from .models import Thread,Post,Club,Fecha
# Register your models here.

admin.site.register(Thread)
admin.site.register(Post)
admin.site.register(Club)
admin.site.register(Fecha)