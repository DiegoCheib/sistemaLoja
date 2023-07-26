"""
URL configuration for thedjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


'''
robs tutoriais!

Aqui nesse arquivo a gente adicona um import olha aqui em cima e voce vai entender a logica.
exemplo: linha 19 -> from users(pasta do app users).views(arquivo onde criamos a funcao da view/tela) import Xview,Yview...

'''
# Aqui declaramos urlpatterns que eh uma lista que vai receber funcoes path onde criaremos um url 
# melhor sem .html no fim de cada pagina
# e em seguida no formato (str(url), funcao(tela), facilitarProsAmiguinhos(nome))
# eh isso...
# recomendo voce ler o src/thedjango/settings.py la tem mt info E LE A PORRA DA DOCUMENTACAO DO DJANGO DESGRACA


urlpatterns = [
    path('login/', include("users.urls"), name="FormsViews"),
    path('admin/', admin.site.urls, name="administration"),
]
