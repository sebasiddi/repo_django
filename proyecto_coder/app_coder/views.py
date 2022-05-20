from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Curso
from django.template import loader
# Create your views here.

"""
def curso(request):
    cursos = Curso.objects.all()
    return HttpResponse(cursos)
"""
def alta_curso(request,nombre):
    curso = Curso(nombre=nombre,camada=21515)
    curso.save()
    texto = f"se guardó en la DB el curso {curso.nombre} camada {curso.camada}"
    return HttpResponse(texto)

def inicio(request):
    return render(request,"template/plantilla.html")

def curso(request):
    cursos = Curso.objects.all()
    dicc = {"cursos":cursos}
    plantilla = loader.get_template("template/plantilla.html")
    documento=plantilla.render(dicc)
    return HttpResponse(documento)




