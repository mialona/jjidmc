from django.contrib import admin
from .models import Configuracion, Edicion, Presentacion

class EditionAdmin(admin.ModelAdmin):
  list_display = ("curso",)

class PresentationAdmin(admin.ModelAdmin):
  list_display = ("titulo","autor","edicion",)

# Register your models here.
admin.site.register(Configuracion)
admin.site.register(Edicion, EditionAdmin)
admin.site.register(Presentacion, PresentationAdmin)