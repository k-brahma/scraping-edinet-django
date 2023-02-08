from django.views.generic import ListView
from .models import SecCodeList


# Create your views here.
class SecCodeListV(ListView):
    model = SecCodeList
    template_name = 'sec_code_list.html'
