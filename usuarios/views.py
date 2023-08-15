from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            messages.info(request, 'Este username já existe')
            return render(request, 'cadastro.html')

        user = User.objects.create_user(first_name=nome, last_name=sobrenome, username=username, email=email, password=senha)  # noqa
        user.save()
        messages.info(request, 'Usuário cadastrado com sucesso')
        return render(request, 'login.html')


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            return render(request, 'pagina_inicial.html')
        else:
            messages.info(request, 'Usuário ou senha inválidos')
            return render(request, 'login.html')


@login_required(login_url="/auth/login/")
def sair(request):
    logout(request)
    return render(request, 'pagina_inicial.html')
