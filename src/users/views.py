from django.shortcuts import render


# Create your views here.

# Funcoes declaradas aqui sao telas do app "USERS" que no caso eh onde cadastramos users
# Para usar as telas declaradas aqui voce vai no diretorio src/diretoriododjango (thedjango) no caso/urls.py
# e la vou deixar mais informacao

#Login screen
def login_view(request, *args, **kwargs):
    return render(request, "login.html", {})

#1st sigtnup screen
def signup1_view(request, *args, **kwargs):
    return render(request, "signup.html", {})

def signup2_view(request, *args, **kwargs):
    return render(request, "signup2.html", {})