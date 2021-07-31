from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Materia)
class AdminTry(admin.ModelAdmin):
    list_display = ['materia']
    list_filter = ['materia']
    search_fields = ['materia']

    class Meta:
        model = Materia

@admin.register(Domanda)
class DomandaAdmin(admin.ModelAdmin):
    readonly_fields = ('username',)
    list_display = ['domanda', 'prof', 'materia','username']
    list_filter = ['prof', 'materia', 'username']
    search_fields = ['domanda', 'prof', 'materia']