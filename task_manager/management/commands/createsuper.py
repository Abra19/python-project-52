import os
from dotenv import load_dotenv
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

load_dotenv()


class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not User.objects.filter(
            username=os.getenv('DJANGO_SUPERUSER_USERNAME')
        ).exists():
            User.objects.create_superuser(
                username=os.getenv('DJANGO_SUPERUSER_USERNAME'),
                password=os.getenv('DJANGO_SUPERUSER_PASSWORD'),
                email=os.getenv('DJANGO_SUPERUSER_EMAIL'),
            )
        print('Superuser has been created.')
