from django.shortcuts import render

def tela_login(request):
    return render(request, 'tela_login.html')
