from django.views.generic import ListView
from .models import SeccodeList


# Create your views here.
class Seccodelistv(ListView):
    model = SeccodeList
    template_name = 'seccode_list.html'
