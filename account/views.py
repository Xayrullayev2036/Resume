import mimetypes
from django.http.response import HttpResponse
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


class ComponentsView(TemplateView):
    template_name = "components.html"



