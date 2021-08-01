from django.urls import path
from django.views.generic import ListView, DetailView
from .models import *
from .views import send_question
import random
from .views import QuestionsView, MaterieView, RandomQuestionAPI


urlpatterns = [
    path('', MaterieView.as_view(paginate_by=12), name='materie'), #Lista di tutte le materie

    path('send/', send_question, name='sendquestion'),

    path('random_api/<str:subject>/', RandomQuestionAPI.as_view(), name='random_api'),

    path('<str:materia>/<int:pk>/', DetailView.as_view(
        queryset=Domanda.objects, template_name="domande/single.html"), name='single'), # Post singoli

    # path('ciao', funzionecheritornailjson, name='api')
    path('<str:materia>/', QuestionsView.as_view(paginate_by=20), name='list'), #lista delle domande

]
