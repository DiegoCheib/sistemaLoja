from django.shortcuts import render
from django import forms
from .forms import inputName
from .models import userTest as useradd
from django.urls import reverse
import pytest
from django.http import HttpResponseRedirect

# Create your views here.
global listacheckform


def signup1_view(request, *args, **kwargs):
    if request.method == "POST":
        nome = inputName(request.POST)
        sobrenome = inputName(request.POST)
        if nome.is_valid() and sobrenome.is_valid():
            nome = nome.cleaned_data['nome']
            sobrenome = sobrenome.cleaned_data["sobrenome"]
            user_new = useradd()
            user_new.username, user_new.usersobrenome = nome, sobrenome
            user_new.save()
    else:
        nome      = inputName()
        sobrenome = inputName()
    
    return render(request, "signup.html", {
        "inputnome": nome,
    })

def signup2_view(request, *args, **kwargs):
    return render(request, "signup2.html", {})