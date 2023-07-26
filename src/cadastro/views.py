from django.shortcuts import render

# Create your views here.



def signup1_view(request, *args, **kwargs):
    return render(request, "signup.html", {})

def signup2_view(request, *args, **kwargs):
    return render(request, "signup2.html", {})