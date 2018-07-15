from django.contrib import admin
from .models import Thread,Post,Club,Fecha,Archivo,Recurso,Plantas
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display= ('owner','date','reply_to','content','aprobado')
    list_filter= ('owner','date','aprobado')
    search_fields= ('owner','date')
    date_hierarchy= 'date'
    ordering= ['aprobado','date','owner']

class ThreadAdmin(admin.ModelAdmin):
    list_display= ('op','category','topic','respuestas')
    list_filter= ('category','topic','respuestas')
    search_fields= ('category','topic')
    ordering= ['category','respuestas']

admin.site.register(Thread,ThreadAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Plantas)
admin.site.register(Club)
admin.site.register(Fecha)
#admin.site.register(Archivo)
#admin.site.register(Recurso)
