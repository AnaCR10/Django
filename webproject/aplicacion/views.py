from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'aplicacion/index.html')#con esto llama a la página web
   # return HttpResponse(" --- Mi primera página Django!!! --- ")

def viernes(request):
    return HttpResponse(" -- POR FIN ES VIERNES!!! --")

def metodoViernes(request):
    return render(request,'aplicacion/viernes.html')

