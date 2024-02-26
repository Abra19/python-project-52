from django.views.generic.base import TemplateView
from task_manager import texts


class BasicView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['basic'] = texts.basic
        return context


class IndexView(BasicView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['texts'] = {
            'hexlet_hello': texts.hexlet_hello,
            'hexlet_practice': texts.hexlet_practice,
            'see_more': texts.see_more,
        }
        return context


class Error500View(BasicView):
    template_name = './errors/error_500.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['errors'] = {
            'error_occurs': texts.error_occurs,
            'we_know': texts.we_know,
            'return_on_index': texts.return_on_index,
        }
        return context


class Error404View(BasicView):
    template_name = './errors/error_404.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['errors'] = {
            'not_found': texts.not_found,
            'very_complicate': texts.very_complicate,
            'return_on_index': texts.return_on_index,
        }
        return context
