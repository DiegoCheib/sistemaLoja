from django.urls import path
from cadastro import views

app_name = "cadastro"

urlpatterns = [
    path('', views.signup1_view, name='signupview1'),
    path('final', views.signup2_view, name='signupview2'),
    path('done', views.signupdone, name='cadastrado')
]