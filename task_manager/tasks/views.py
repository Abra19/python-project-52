from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django_filters.views import FilterView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from task_manager.users.models import User
from task_manager.tasks.models import Task
from task_manager.tasks.forms import TaskForm
from task_manager.tasks.filters import TaskFilter
from task_manager import texts
from task_manager.custom_mixins import AuthCheckMixin, AuthorCheckMixin


class TasksListView(AuthCheckMixin, FilterView):
    """
    List of tasks
    Access only for auth users
    """
    template_name = 'tasks/tasks.html'
    model = Task
    filterset_class = TaskFilter
    context_object_name = 'tasks'

    extra_context = {
        'basic': texts.basic,
        'texts': texts.create_tasks,
        'button_text': texts.buttons['demonstrate']
    }


class TaskView(AuthCheckMixin, DetailView):
    """
    Show task details

    Authorisation required.
    """
    template_name = 'tasks/task_detail.html'
    model = Task
    context_object_name = 'task'
    extra_context = {
        'basic': texts.basic,
        'texts': texts.create_tasks,
    }


class TaskCreateView(AuthCheckMixin, SuccessMessageMixin, CreateView):
    """
    Create new Task by TaskForm
    Form valid method is called when the form is valid
    It's overridden to set the current user as the author of the task
    Redirect to tasks
    Make message about success with SuccessMessageMixin
    Only for authorized users
    """
    pass
    template_name = 'form.html'
    model = Task
    form_class = TaskForm

    success_url = reverse_lazy('tasks')
    success_message = texts.messages['task_created']

    extra_context = {
        'basic': texts.basic,
        'title': texts.create_tasks['task_create'],
        'button_text': texts.buttons['create_label']
    }

    def form_valid(self, form):
        form.instance.author = User.objects.get(pk=self.request.user.pk)
        return super().form_valid(form)


class TaskUpdateView(AuthCheckMixin, SuccessMessageMixin, UpdateView):
    """
    Change task by TaskForm
    In success redirect to list of statuses and make message
    about success with SuccessMessageMixin
    Only for authorized users
    """
    template_name = 'form.html'
    model = Task
    form_class = TaskForm

    success_url = reverse_lazy('tasks')
    success_message = texts.messages['task_changed']

    extra_context = {
        'basic': texts.basic,
        'title': texts.create_tasks['task_update_title'],
        'button_text': texts.buttons['update_button']
    }


class TaskDeleteView(
    AuthCheckMixin,
    AuthorCheckMixin,
    SuccessMessageMixin,
    DeleteView
):
    """
    Delete existing task
    In success redirect to list of tasks and make message
    If author of task is not current user it cannot be deleted
    Only for authorized users
    """
    template_name = 'delete.html'
    model = Task

    success_url = reverse_lazy('tasks')
    success_message = texts.messages['task_deleted']

    permission_message = texts.messages['protected_task']
    permission_url = reverse_lazy('tasks')

    extra_context = {
        'basic': texts.basic,
        'title': texts.create_tasks['task_delete_title'],
        'delete_sure': texts.delete_user['delete_sure'],
        'dest_url': reverse_lazy('tasks'),
        'delete_cancel': texts.create_tasks['task_detail_cancel'],
        'button_text': texts.buttons['delete_button']
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['delete_obj'] = self.get_object().name
        return context
