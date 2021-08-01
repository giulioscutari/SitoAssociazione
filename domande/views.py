from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import FormDomanda
from .models import Domanda
# from django.http import JsonResponse

# Create your views here.

@login_required
def send_question(request):

    if request.method == 'POST':
        form = FormDomanda(request.POST, initial={"username": request.user.username})
        if form.is_valid():
            form.save()
            messages.info(request, f'Le tue domande sono state inoltrate. Grazie')
    else:
        form = FormDomanda(initial={"username": request.user.username})
    
    return render(request, 'domande/sendquestion.html', {'form': form, "username": request.user.username})



# def ciao(request):

#     return JsonResponse({
#         "hello": "culo"
#     })