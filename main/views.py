from django.views.generic import TemplateView


# Create your views here.
class TopView(TemplateView):
    """トップページ"""
    template_name = "index.html"
