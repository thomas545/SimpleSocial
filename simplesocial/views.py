from django.views.generic import TemplateView



class TestPage(TemplateView):
    template_name = 'test.html'


class ThnaksPage(TemplateView):
    template_name = 'thanks.html'


class HomeView(TemplateView):
    template_name = 'index.html'
