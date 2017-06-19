from django.shortcuts import render
from django.http import HttpResponse

from .models import Seleccion

def index(request):
    selecciones = Seleccion.objects.order_by('nombre')
    context = {'selecciones': selecciones}
    #output = ', '.join([s.nombre for s in selecciones])
    return render(request, 'confederaciones/index.html', context)
    #return HttpResponse(output)