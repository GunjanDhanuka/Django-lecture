from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def gunjan(request):
    return HttpResponse("Hello, Gunjan!")

def niyati(request):
    return HttpResponse("Hello, Niyati")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    }
    )