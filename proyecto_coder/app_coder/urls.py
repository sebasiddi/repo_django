from django.urls import URLPattern, path
from . import views

urlpatterns = [
        path("Cursos", views.curso),
        path("alta_curso/<nombre>", views.alta_curso)

]