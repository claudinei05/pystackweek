from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def cadastro_medico(request):
    if request.method == "GET":
        return render(request, 'cadastro_medico.html')