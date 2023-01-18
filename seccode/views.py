from django.views.generic import  ListView
from .models import seccode_list

# Create your views here.
class seccode_list(ListView):
    model = seccode_list
    template_name = 'seccode/seccode_list.html'
    context_object_name = 'seccode_list'

    def get_queryset(self):
        return seccode_list.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context