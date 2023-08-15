from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/auth/login/")
def pagina_inicial(request):
    return render(request, 'pagina_inicial.html')
