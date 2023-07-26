from django.urls import path

from . import views

urlpatterns = [
    path('', views.signup1_view, name='signupview1'),
    path('final', views.signup2_view, name='signupview2')
]