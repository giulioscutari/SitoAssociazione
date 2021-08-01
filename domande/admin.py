from django.contrib import admin
from .models import *

# Register your models here.
def make_published(modeladmin, request, queryset):
    queryset.update(status='Published')
make_published.short_description = "Pubblica la(e) domanda(e)"

def make_draft(modeladmin, request, queryset):
    queryset.update(status='Draft')
make_draft.short_description = "Non pubblicare la(e) domanda(e) selezionata(e)"


@admin.register(Materia)
class AdminTry(admin.ModelAdmin):
    list_display = ['materia']
    list_filter = ['materia']
    search_fields = ['materia']

    class Meta:
        model = Materia

@admin.register(Domanda)
class DomandaAdmin(admin.ModelAdmin):
    actions = [make_published, make_draft]
    readonly_fields = ('username','status')
    list_display = ['domanda', 'prof', 'materia','username', 'status']
    list_filter = ['prof', 'materia', 'username']
    search_fields = ['domanda', 'prof', 'materia', 'status']

    class Meta:
        model = Domanda