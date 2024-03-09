from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from task_manager.labels.models import Label
from task_manager.labels.forms import LabelForm
from task_manager import texts
from task_manager.custom_mixins import AuthCheckMixin, ProtectDeleteMixin


class LabelsListView(ListView):
    """
    List of labels
    Access only for auth users
    """
    template_name = 'labels/labels.html'
    model = Label
    context_object_name = 'labels'

    extra_context = {
        'basic': texts.basic,
        'texts': texts.create_label,
    }


class LabelCreateView(AuthCheckMixin, SuccessMessageMixin, CreateView):
    """
    Create new label by LabelForm
    Redirect to labels
    Make message about success with SuccessMessageMixin
    Only for authorized users
    """
    template_name = 'form.html'
    model = Label
    form_class = LabelForm

    success_url = reverse_lazy('labels')
    success_message = texts.messages['label_created']

    extra_context = {
        'basic': texts.basic,
        'title': texts.create_user['label_create'],
        'button_text': texts.buttons['create_label']
    }


class LabelUpdateView(AuthCheckMixin, SuccessMessageMixin, UpdateView):
    """
    Change label by LabelForm
    In success redirect to list of labels and make message
    about success with SuccessMessageMixin
    Only for authorized users
    """
    template_name = 'form.html'
    model = Label
    form_class = LabelForm

    success_url = reverse_lazy('labels')
    success_message = texts.messages['label_changed']

    extra_context = {
        'basic': texts.basic,
        'title': texts.create_label['label_change_title'],
        'button_text': texts.buttons['update_button']
    }


class LabelDeleteView(
    AuthCheckMixin,
    ProtectDeleteMixin,
    SuccessMessageMixin,
    DeleteView
):
    """
    Delete existing label.
    In success redirect to list of labels and make message
    If the label is associated with at least one task it cannot be deleted.
    Only for authorized users
    """
    template_name = 'delete.html'
    model = Label

    success_url = reverse_lazy('labels')
    success_message = texts.messages['label_deleted']

    protected_message = texts.messages['protected_label']
    protected_url = reverse_lazy('labels')

    extra_context = {
        'basic': texts.basic,
        'title': texts.create_label['label_delete_title'],
        'delete_sure': texts.delete_user['delete_sure'],
        'dest_url': reverse_lazy('labels'),
        'delete_cancel': texts.create_label['back_to_labels'],
        'button_text': texts.buttons['delete_button']
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['delete_obj'] = self.get_object().name
        return context
