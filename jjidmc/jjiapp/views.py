from django.http import HttpResponse
from django.template import loader
from .models import Configuracion, Edicion, Presentacion

def home(request):
  config = Configuracion.objects.all()[0]
  participacion = config.participacion.splitlines()
  formato = config.formato.splitlines()
  ediciones = Edicion.objects.all().values()
  presentaciones = Presentacion.objects.all().values()
  template = loader.get_template('home.html')
  context = {
    'collapse': True,
    'configuracion': config,
    'participacion': participacion,
    'formato':formato,
    'ediciones': ediciones,
  }
  return HttpResponse(template.render(context, request))

def edition(request, curso):
  edicion = Edicion.objects.get(curso = curso)
  titulo = edicion.titulo
  descripcion = edicion.descripcion.splitlines()
  parners = edicion.parners.splitlines()
  dias = [x[0] for x in Presentacion.objects.filter(edicion = edicion).values_list('fecha').distinct().order_by('fecha')]
  presentaciones = []
  for x in dias:
    presentaciones.append(Presentacion.objects.filter(fecha=x.strftime('%Y-%m-%d')).order_by('hora_inicio').values())
  template = loader.get_template('edition.html')
  context = {
    'collapse': False,
    'curso': str(curso),
    'titulo': titulo,
    'descripcion': descripcion,
    'parners': parners,
    'presentaciones': presentaciones,
    'dias': dias,
  }
  return HttpResponse(template.render(context, request))

def presentation(request, curso, id):
  presentacion = Presentacion.objects.get(id = id)
  abstract = presentacion.abstract.splitlines()
  template = loader.get_template('presentation.html')
  context = {
    'collapse': False,
    'presentacion': presentacion,
    'abstract': abstract,
  }
  return HttpResponse(template.render(context, request))