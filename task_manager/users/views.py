from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from task_manager.users.models import User
from task_manager.users.forms import UserForm, UpdateUserForm
from task_manager import texts
from task_manager.custom_mixins import AuthCheckMixin, PermissionCheckMixin


class UserCreateView(SuccessMessageMixin, CreateView):
    """
    Register new user by registration form - UserForm
    Redirect to login page
    Make message about success with SuccessMessageMixin
    """
    template_name = 'registration.html'
    model = User
    form_class = UserForm
    extra_context = {
        'basic': texts.basic,
        'create': texts.create_user,
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
    Change user datas by registration form - UpdateUserForm
    Using UpdateUserForm allows to make changes while keeping the old username
    In success redirect to list of users and make message about success with SuccessMessageMixin
    User can only edit himself - if edit other user redirect to permission_url
    and make permission_message about error with PermissionCheckMixin
    """
    template_name = 'registration.html'
    model = User
    form_class = UpdateUserForm

    success_url = reverse_lazy('users')
    success_message = texts.messages['success_update']

    permission_message = texts.messages['no_rights']
    permission_url = reverse_lazy('users')

    extra_context = {
        'basic': texts.basic,
        'create': texts.create_user,
        'list': texts.users_list,
        'button_text': texts.buttons['update_button']
    }


class UserDeleteView(
    AuthCheckMixin,
    PermissionCheckMixin,
    SuccessMessageMixin,
    DeleteView
):
    """
    Delete existing user.
    In success redirect to list of users and make message about success with SuccessMessageMixin
    User can only delete himself - if delete other user redirect to permission_url
    and make permission_message about error with PermissionCheckMixin
    """
    template_name = 'users/delete.html'
    model = User

    success_url = reverse_lazy('users')
    success_message = 'User is successfully deleted'

    permission_message = 'You have no rights to change another user.'
    permission_url = reverse_lazy('users')

    extra_context = {
        'basic': texts.basic,
        'delete_user': texts.delete_user,
        'button_text': texts.buttons['delete_button']
    }