from domande.models import Materia
from django.views.generic import ListView


class MaterieView(ListView):
    context_object_name = 'materie'
    template_name = "domande/materie.html"

    def get_queryset(self):
        return Materia.objects.all()
