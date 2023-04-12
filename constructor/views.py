from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def constructor(request):
    return render(request, 'constructor.html')

def prueba(request):
    return render(request, 'prueba1.html')