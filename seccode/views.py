from django.views.generic import ListView
from .models import SecCodeList


# Create your views here.
class SecCodelistv(ListView):
    model = SecCodeList
    template_name = 'seccode_list.html'
