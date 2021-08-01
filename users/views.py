from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import Profile


# def my_login_required(function):
#     def wrapper(request, *args, **kw):
#         user=request.user  
#         if not (user.id and Profile.objects.get(user=user).status):
#             return redirect('/login')
#         else:
#             return function(request, *args, **kw)
#     return wrapper


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            if form.cleaned_data.get('email').split('@')[1] == 'studenti.uniroma1.it':
                user = form.save()
                user.is_active = False
                user.name = form.cleaned_data.get('nome')
                user.surname = form.cleaned_data.get('cognome')
                user.save()
                return redirect('login')
            else:
                messages.error(request, 'Per favore utilizza la tua mail istituzionale @studenti.uniroma1.it')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
