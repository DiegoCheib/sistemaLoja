from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
def menuView(request, *args, **kwargs):
    '''
    Esta funcao cria a view para ser renderizada no home.urls.py
    '''
    return render(request, "menu.html", {})