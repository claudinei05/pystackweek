from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')        
    elif request.method == "POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        senha=request.POST.get('senha')
        confirmar_senha=request.POST.get('confirmar_senha')

        if senha != confirmar_senha:
            print("ERRO 2: O campo senha e confirme senha não são iguais")
            return redirect('/usuarios/cadastro')
        
        if len(senha) < 6:
            print('ERRO 3: Senha precisa de no minimo 6 caracteres')
            return redirect('/usuarios/cadastro')
        
        users= User.objects.filter(username=username)
        print(users.exists())

        if users.exists():
            print("ERRO 1 Usuario ja existe")
            return redirect('/usuarios/cadastro')
        
        user=User.objects.create_user(
            username=username,
            email=email,
            password=senha
        )
        
        return HttpResponse(f'Usuario criado com sucesso')
    