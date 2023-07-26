from django.shortcuts import render


#Login screen
def login_view(request, *args, **kwargs):
    return render(request, "login.html", {})

