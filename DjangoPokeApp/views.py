from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {'clase': 'Aprendiendo Django'}
    return render(request, 'types_list.html', context)

# Create your views here.
