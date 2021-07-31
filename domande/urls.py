from django.urls import path
from django.views.generic import ListView, DetailView
from .models import *
from .views import send_question
import random


class QuestionsView(ListView):
    context_object_name = 'domande'
    template_name = "domande/list.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Domanda.objects.filter(materia__materia=self.kwargs['materia'], # status='Published'
        ).order_by('-punteggio')


class MaterieView(ListView):
    context_object_name = 'materie'
    template_name = "domande/materie.html"

    def get_queryset(self):
        return Materia.objects.all()

urlpatterns = [
    path('', MaterieView.as_view(paginate_by=12), name='materie'), #Lista di tutte le materie

    path('send/', send_question, name='sendquestion'),

    path('<str:materia>/', 
    QuestionsView.as_view(paginate_by=20), 
    name='list'), #lista delle domande

    path('<str:materia>/<int:pk>/', DetailView.as_view(
        queryset=Domanda.objects, template_name="domande/single.html"), name='single'), # Post singoli

]
