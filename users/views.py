from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            if form.cleaned_data.get('email').split('@')[1] == 'studenti.uniroma1.it':
                messages.error(request, f'Your account has been created! You are now able to log in')
                form.save()
                return redirect('login')
            else:
                messages.error(request, 'Per favore utilizza la tua mail istituzionale @studenti.uniroma1.it')
    else:
        form = UserRegisterForm()
    print('Not right email')
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
