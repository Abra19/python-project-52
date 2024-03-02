from django.views.generic import CreateView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from task_manager.users.models import User
from task_manager.users.forms import UserForm
from task_manager import texts


class UserCreateView(SuccessMessageMixin, CreateView):
    """
    Register new user by registration form
    Redirect to login page
    Make message about success with SuccessMessageMixin
    """
    template_name = 'registration.html'
    model = User
    form_class = UserForm
    extra_context = {
        'basic': texts.basic,
        'texts': texts.create_user,
    }
    success_url = reverse_lazy('login')
    success_message = texts.messages['user_created']


class UsersListView(ListView):
    pass