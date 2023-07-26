from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name="login_view"),
    path('signup', views.signup1_view, name="first_signup_form"),
    path('signup2', views.signup2_view, name="Second_signup_form")
]