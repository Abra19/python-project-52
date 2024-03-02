from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import activate
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from task_manager import texts


def set_language(request, language):
    activate(language)
    response = HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    response.set_cookie('django_language', language)
    return response


class BasicView(TemplateView):
    extra_context = {
        'basic': texts.basic,
        'texts': texts.index,
        'errors': texts.errors,
    }


class IndexView(BasicView):
    template_name = 'index.html'


class UserLoginView(SuccessMessageMixin,LoginView):
    """
    Login user by login form
    Redirect to home page for authorized users
    Make message about success with SuccessMessageMixin
    """
    template_name = 'login.html'
    form_class = AuthenticationForm
    extra_context = {
        'basic': texts.basic,
        'login': texts.login,
    }
    next_page = reverse_lazy('home')
    success_message = texts.messages['logged']

class UserLogoutView(LogoutView):
    success_url = reverse_lazy('home')
    success_message = texts.messages['logout']

    def get_success_url(self):
        return self.success_url

    def dispatch(self, request, *args, **kwargs):
        messages.success(self.request, texts.messages['logout'])
        return super().dispatch(request, *args, **kwargs)


class Error500View(BasicView):
    template_name = './errors/error_500.html'


class Error404View(BasicView):
    template_name = './errors/error_404.html'
