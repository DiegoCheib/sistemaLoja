from django.shortcuts import render
from django import forms
from .forms import inputName, inputSobrenome
from .models import userTest as useradd
from django.urls import reverse
import pytest
from django.http import HttpResponseRedirect

# Create your views here.
global listacheckform


def signup1_view(request, *args, **kwargs):
    # se o client der submit o metodo do requeste se torna POST logo entramos no if
    if request.method == "POST":
        # Dentro do if criei duas instancias de dois inputs que recebem nome declarados em cadastro.forms
        nome = inputName(request.POST)
        sobrenome = inputSobrenome(request.POST)
        # Se os parametros html declarados no cadastro.forms forem validados com -> 
        if nome.is_valid() and sobrenome.is_valid():
            nome = nome.cleaned_data['nome']
            sobrenome = sobrenome.cleaned_data["sobrenome"]
            user_new = useradd()
            user_new.username, user_new.usersobrenome = nome, sobrenome
            user_new.save()
    else:
        nome      = inputName()
        sobrenome = inputSobrenome()
    
    return render(request, "signup.html", {
        "inputnome": nome,
        "inputsobrenome" : sobrenome,
    })

def signup2_view(request, *args, **kwargs):
    return render(request, "signup2.html", {})