from django.views.generic import TemplateView
from ProjetoOlaMundo.models import Paciente
from django.views.generic.edit import CreateView

class Index(TemplateView):
    template_name ="index.html"
    
class CriaFuncionario(CreateView): 
    template_name = "index.html"   
    model = Paciente()
    fields = '__all__'
