from django.db import models
from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from task_manager.texts import create_tasks


class Task(models.Model):
    name = models.CharField(
        max_length=150,
        blank=False,
        unique=True,
        verbose_name=create_tasks['task_name']
    )
    description = models.TextField(
        max_length=1000,
        blank=True,
        verbose_name=create_tasks['task_description']
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=create_tasks['task_date']
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name=create_tasks['task_author'],
        related_name='author'
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        verbose_name=create_tasks['task_status']
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name=create_tasks['task_executor'],
        related_name='executor'
    )
    labels = models.ManyToManyField(
        Label,
        through='TaskLabelLinks',
        through_fields=('task', 'label'),
        blank=True,
        verbose_name=create_tasks['task_labels']
    )


class TaskLabelLinks(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)
