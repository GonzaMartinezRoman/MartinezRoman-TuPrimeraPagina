from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return HttpResponse("Hola, este es mi primer proyecto con Django y lo hice en el curso de CoderHouse")
