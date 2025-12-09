from django.apps import AppConfig
from django.contrib.auth.models import Group, Permission
from django.apps import apps
from django.db.models.signals import post_migrate

class BookshelfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookshelf'

def create_groups(sender, **kwargs):
    Book = apps.get_model('bookshelf', 'Book')
    permissions = Permission.objects.filter(content_type__app_label='bookshelf', content_type__model='book')

    editors, _ = Group.objects.get_or_create(name='Editors')
    viewers, _ = Group.objects.get_or_create(name='Viewers')
    admins, _ = Group.objects.get_or_create(name='Admins')

    # Assign permissions
    editors.permissions.set(permissions.filter(codename__in=['can_create', 'can_edit']))
    viewers.permissions.set(permissions.filter(codename__in=['can_view']))
    admins.permissions.set(permissions)  # all permissions

post_migrate.connect(create_groups)