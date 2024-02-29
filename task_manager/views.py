from django.http import HttpResponseRedirect
from django.utils.translation import activate
from django.views.generic.base import TemplateView
from task_manager import texts

def set_language(request, language):
    activate(language)
    response = HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    response.set_cookie('django_language', language)
    return response


class BasicView(TemplateView):
    extra_context = {
        'basic': texts.basic,
        'texts': {
            'hexlet_hello': texts.hexlet_hello,
            'hexlet_practice': texts.hexlet_practice,
            'see_more': texts.see_more,
        },
        'errors': {
            'error_occurs': texts.error_occurs,
            'we_know': texts.we_know,
            'not_found': texts.not_found,
            'very_complicate': texts.very_complicate,
            'return_on_index': texts.return_on_index,
        }
    }


class IndexView(BasicView):
    template_name = 'index.html'


class Error500View(BasicView):
    template_name = './errors/error_500.html'


class Error404View(BasicView):
    template_name = './errors/error_404.html'
