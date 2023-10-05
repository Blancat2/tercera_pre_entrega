from django.shortcuts import render
from models import Equipo, Camisetas, Copas
from django.http import HttpResponse

def equipoForms(request):
    if request.method == 'POST':
        equipo = Equipo (request.post['equipo'], (request.post['Año']))
        equipo.save()
        return render(request, "index.html")
    return render(request, "templates/equipos.html")

def camisetasForms(request):
    
    return render (request, "templates/camisetas.html")

def buscar(request):
    if request.GET["num_copa"]:
        num_copa = request.GET['num_copa']
        copa = Copas.objects.filter(num_copa__icontains=num_copa)

        return render(request, "copas.html", {"copa":copa, "num_copa":num_copa})
    
    else:
        respuesta= "Datos Invalidos"

    return HttpResponse(respuesta)
        

def copasForms(request):
    return render (request, "templates/copas.html")