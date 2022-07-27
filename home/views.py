from django.views.generic import TemplateView

class IndexView(TemplateView):
    """
    A view to return the index page, rendered on the index.html template.
    """
    template_name = 'home/index.html'