from django.views.generic import ListView
from .models import seccode_list

# Create your views here.
class Seccodelistv(ListView):
    model = seccode_list
    template_name = 'seccode_list.html'
