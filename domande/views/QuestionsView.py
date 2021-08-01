from domande.models import Domanda
from django.views.generic import ListView

class QuestionsView(ListView):
    context_object_name = 'domande'
    template_name = "domande/list.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Domanda.objects.filter(materia__materia=self.kwargs['materia'], status='Published'
        ).order_by('-punteggio')
