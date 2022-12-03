from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Tabla de tipos")

# Create your views here.
