from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Bruno Schuster',
    })

def contato(request):
    return HttpResponse('recipes/contato.html')

def sobre(request):
    return HttpResponse('sobre')