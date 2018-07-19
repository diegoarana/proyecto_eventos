from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view

def index(request):
    return render(request, 'index.html')


@api_view(['POST'])
def confirmarAsistencia(request):
    if request.is_ajax:
        # taking values fom POST request
        nombre_apellido = request.POST.get['nombre-apellido']
        email = request.POST.get['email']
        mensaje = request.POST.get['mensaje']
        # creating a guest
        evento = Evento.objects.first()
        invitado = Invitado(evento=evento, nombre_apellido=nombre_apellido, email=email, mensaje=mensaje)
        invitado.save()
        data_json='ok'

    else:
        data_json='fail'
    mimetype="application/json"
    return HttpResponse(data_json, mimetype)