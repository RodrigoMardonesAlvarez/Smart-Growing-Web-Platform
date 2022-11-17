from django.contrib import admin
from .models import Tag, Entrada

# Register your models here.

class TagAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class EntradaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Tag, TagAdmin)
admin.site.register(Entrada, EntradaAdmin)