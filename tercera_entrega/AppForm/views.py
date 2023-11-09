from django.shortcuts import render
from .models import Equipos, Camisetas, Copas
from django.http import HttpResponse

def equipoForms(request):
    if request.method == 'POST':
        equipo = Equipos (request.post['equipos'], (request.post['Año']))
        equipo.save()
        return render(request, "index.html")
    return render(request, "equipos.html")

def camisetasForms(request):
    if request.method == 'POST':
        camisetas = Camisetas (request.post['nom_equipo'], (request.post['ano_camiseta']))
        camisetas.save()
        return render(request, "index.html")
    return render(request, "camisetas.html")


    
    

def buscar(request):
    if request.GET["num_copa"]:
        num_copa = request.GET['num_copa']
        copa = Copas.objects.filter(num_copa__icontains=num_copa)

        return render(request, "copas.html", {"copa":copa, "num_copa":num_copa})
    
    else:
        respuesta= "Datos Invalidos"

    return HttpResponse(respuesta)
        

def copasForms(request):
    return render (request, "copas.html")