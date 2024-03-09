from django.utils.translation import gettext_lazy as _


basic = {
  'app_title': _('App title'),
  'task_manager': _('Task Manager'),
  'users': _('Users'),
  'login': _('Login'),
  'register': _('Register'),
  'hexlet': _('Hexlet'),
  'statuses': _('Statuses'),
  'labels': _('Labels'),
  'tasks': _('Tasks'),
  'exit': _('Exit'),
}

index = {
  'hexlet_hello': _('Hexlet hello'),
  'hexlet_practice': _('Hexlet practice'),
  'see_more': _('See more'),
}

create_user = {
  'first_name': _('First_name'),
  'last_name': _('Last_name'),
  'register': _('Register'),
  'update_title': _('Update title'),
  'label_create': _('Label create'),
}

buttons = {
  'create_button': _('Button create'),
  'update_button': _('Button update'),
  'delete_button': _('Button delete'),
  'create_status': _('Create status button'),
  "create_label": _('Create label button'),
}

users_list = {
  'list_title': _('List_title'),
  'id': _('ID'),
  'user_name': _('Using name'),
  'full_name': _('Full name'),
  'date_joined': _('Date joined'),
  'update': _('Update'),
  'delete': _('Delete'),
}

delete_user = {
  'delete_title': _('Delete title'),
  'delete_sure': _('Delete sure'),
  'delete_cancel': _('Delete cancel'),
}

login = {
  'enter': _('Enter'),
  'enter_text': _('Enter_text'),
}

create_status = {
  'status_name': _('Status name'),
  'status_title': _('Status title'),
  'status_create': _('Create status'),
  'status_id': _('Status ID'),
  'status_date': _('Status date'),
  'status_update': _('Update status'),
  'status_delete': _('Delete status'),
  'status_change_title': _('Change status'),
  'status_delete_title': _('Title delete status'),
  'back_to_statuses': _('Back to the list of statuses'),
}

create_label = {
  'label_name': _('Status name'),
  'label_title': _('Label title'),
  'label_create': _('Create label'),
  'label_id': _('Status ID'),
  'label_date': _('Status date'),
  'label_update': _('Update'),
  'label_delete': _('Delete'),
  'label_change_title': _('Change label'),
  'label_delete_title': _('Title delete label'),
  'back_to_labels': _('Back to the list of labels'),
}

texts = {
  'basic': basic,
  'index': index,
  'create_user': create_user,
  'buttons': buttons,
  'users_list': users_list,
  'delete_user': delete_user,
  'login': login,
  'create_status': create_status,
  'create_label': create_label
}

messages = {
  'user_created': _('User created'),
  'logged': _('Logged'),
  'logout': _('Logout'),
  'no_auth': _('No auth'),
  'success_update': _('Success update'),
  'no_rights': _('No rights'),
  'success_delete': _('Success delete'),
  'status_created': _('Status created'),
  'status_changed': _('Status changed'),
  'status_deleted': _('Status deleted'),
  'protected_status': _('Protected status'),
  'label_created': _('Label created'),
  'label_changed': _('Label changed'),
  'protected_label': _('Protected label'),
  'label_deleted': _('Label deleted'),
}

errors = {
  'error_occurs': _('Error occurs'),
  'we_know': _('We know'),
  'not_found': _('Not found'),
  'very_complicate': _('Very complicate'),
  'return_on_index': _('Return on index'),
}
