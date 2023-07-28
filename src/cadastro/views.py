from django.shortcuts import render, redirect
from django import forms
from .forms import *
from .models import userTest as useradd
from django.urls import reverse
import pytest
from django.http import HttpResponseRedirect

# Create your views here.
'''
user_new = useradd()
user_new.username, user_new.usersobrenome = nome, sobrenome
user_new.save()
'''
def signup1_view(request, *args, **kwargs):
    # se o client der submit o metodo do requeste se torna POST logo entramos no if
    if request.method == "POST":
        # Dentro do if criei duas instancias de dois inputs que recebem nome declarados em cadastro.forms
        nome_input = inputName(request.POST)
        sobrenome_input = inputSobrenome(request.POST)
        # Se os parametros html declarados no cadastro.forms forem validados com -> 
        if nome_input.is_valid() and sobrenome_input.is_valid():
            nome = nome_input.cleaned_data['nome']
            sobrenome = sobrenome_input.cleaned_data['sobrenome']
            request.session['nome'] = nome
            request.session['sobrenome'] = sobrenome
            return redirect('cadastro:signupview2')
                            

    else:
        nome_input      = inputName()
        sobrenome_input = inputSobrenome()
    
    return render(request, "signup.html", {
        "inputnome": nome_input,
        "inputsobrenome" : sobrenome_input,
    })

def signup2_view(request, *args,**kwargs):
    if request.method == "POST":
        email_input = inputEmail(request.POST)
        password_input = inputPassowrd(request.POST)
        phone_input = inputPhone(request.POST)
        cpf_input = inputCpf(request.POST)

        if email_input.is_valid() and password_input.is_valid() and phone_input.is_valid() and cpf_input.is_valid():
            email =  email_input.cleaned_data.get('email')
            password = password_input.cleaned_data['password']
            phone = phone_input.cleaned_data['telefone']
            cpf = cpf_input.cleaned_data['cpf']
            nome = request.session.get('nome')
            sobrenome = request.session.get('sobrenome')
            user_new = useradd()
            user_new.username, user_new.usersobrenome, user_new.useremail, user_new.userpassword, user_new.telefone, user_new.cpf = nome, sobrenome, email, password, phone, cpf
            user_new.save()
            return redirect("cadastro:cadastrado")
    else:
        email_input = inputEmail()
        password_input = inputPassowrd()
        phone_input = inputPhone()
        cpf_input = inputCpf()


    return render(request, "signup2.html", {
        'emailinput': email_input,
        "passwordinput": password_input,
        "phoneinput": phone_input,
        "cpfinput": cpf_input
    })
    
def signupdone(requset, *args, **kwargs):
    return render(requset, 'cadastrado.html', {})