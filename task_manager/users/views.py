from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from task_manager.users.models import User
from task_manager.users.forms import UserForm, UpdateUserForm
from task_manager import texts
from task_manager.custom_mixins import AuthCheckMixin, \
    PermissionCheckMixin, ProtectDeleteMixin


class UserCreateView(SuccessMessageMixin, CreateView):
    """
    Register new user by UserForm
    Redirect to login page
    Make message about success with SuccessMessageMixin
    """
    template_name = 'form.html'
    model = User
    form_class = UserForm
    extra_context = {
        'basic': texts.basic,
        'title': texts.create_user['register'],
        'button_text': texts.buttons['create_button']
    }
    success_url = reverse_lazy('login')
    success_message = texts.messages['user_created']


class UsersListView(ListView):
    """
    List of users
    """
    template_name = 'users/list.html'
    model = User
    context_object_name = 'users'
    extra_context = {
        'basic': texts.basic,
        'list': texts.users_list,
    }


class UserUpdateView(
    AuthCheckMixin,
    PermissionCheckMixin,
    SuccessMessageMixin,
    UpdateView
):
    """
    Change user datas by UpdateUserForm
    Using UpdateUserForm allows to make changes while keeping
    the old username
    In success redirect to list of users and make message
    about success with SuccessMessageMixin
    User can only edit himself - if edit other user redirect
    to permission_url
    and make permission_message about error with PermissionCheckMixin
    """
    template_name = 'form.html'
    model = User
    form_class = UpdateUserForm

    success_url = reverse_lazy('users')
    success_message = texts.messages['success_update']

    permission_message = texts.messages['no_rights']
    permission_url = reverse_lazy('users')

    extra_context = {
        'basic': texts.basic,
        'list': texts.users_list,
        'title': texts.create_user['update_title'],
        'button_text': texts.buttons['update_button']
    }


class UserDeleteView(
    AuthCheckMixin,
    PermissionCheckMixin,
    ProtectDeleteMixin,
    SuccessMessageMixin,
    DeleteView
):
    """
    Delete existing user.
    In success redirect to list of users and make message
    about success with SuccessMessageMixin
    User can only delete himself - if delete other user
    redirect to permission_url
    and make permission_message about error with PermissionCheckMixin
    Can not delete user associated with tasks
    """
    template_name = 'delete.html'
    model = User

    success_url = reverse_lazy('users')
    success_message = texts.messages['success_delete']

    permission_message = texts.messages['no_rights']
    permission_url = reverse_lazy('users')

    protected_message = texts.messages['protected_user']
    protected_url = reverse_lazy('users')

    extra_context = {
        'basic': texts.basic,
        'title': texts.delete_user['delete_title'],
        'delete_sure': texts.delete_user['delete_sure'],
        'dest_url': reverse_lazy('users'),
        'delete_cancel': texts.delete_user['delete_cancel'],
        'button_text': texts.buttons['delete_button']
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            context['delete_obj'] = user.get_full_name()
        return context
