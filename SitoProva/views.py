from django.shortcuts import redirect, reverse, render

def lp(request):
    # if(request.user.is_authenticated):
    #     return redirect(reverse('materie:'))
    return render(request,"index.html")