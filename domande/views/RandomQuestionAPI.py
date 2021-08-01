from django.http.response import JsonResponse
from django.views import View

from domande.models import Domanda
import random
class RandomQuestionAPI(View):

    def get(self, request, subject, *args, **kwargs):
        qs = Domanda.objects.filter(materia__materia=subject, status='Published'
        ).order_by('-punteggio')

        question = random.choice(qs)
        return JsonResponse({
            "domanda": question.domanda,
            "prof": question.prof
        })