

from django.views import View
from django.views.generic import TemplateView

class TopView(TemplateView):
    """トップページ"""
    template_name = "index.html"
