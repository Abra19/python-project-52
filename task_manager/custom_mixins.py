from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import ProtectedError
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from task_manager import texts


class AuthCheckMixin(LoginRequiredMixin):
    """
    Check authentification
    If not - make message about error and redirect to login page
    """

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, texts.messages['no_auth'])
            return redirect(reverse_lazy('login'))
        return super().dispatch(request, *args, **kwargs)


class PermissionCheckMixin(UserPassesTestMixin):
    """
    Test if current user is the owner of the object
    If not - make permission_message and redirect to permission_url
    Concret message and url in corresponding View
    """
    permission_message = None
    permission_url = None

    def test_func(self):
        return self.get_object() == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, self.permission_message)
        return redirect(self.permission_url)


class ProtectDeleteMixin:
    """
    Protect deletion of object in use by other object
    Try to delete object
    If object in use of other object
    make protected_message and redirect to protected_url
    Concret message and url in corresponding View
    """
    protected_message = None
    protected_url = None

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, self.protected_message)
            return redirect(self.protected_url)
