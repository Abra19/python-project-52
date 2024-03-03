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
