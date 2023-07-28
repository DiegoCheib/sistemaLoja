from django.urls import path
from home import views

#aqui declare suas urls

app_name = "home"

urlpatterns = [
    path('', views.menuView, name="menuPrincipal")
]