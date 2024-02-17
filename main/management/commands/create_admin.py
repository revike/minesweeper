from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.management import BaseCommand

from settings.settings import ADMIN_USERNAME, ADMIN_PASSWORD


class Command(BaseCommand):
    """Command to create a superuser"""

    def handle(self, *args, **options):
        if ADMIN_USERNAME and ADMIN_PASSWORD:
            password = make_password(ADMIN_PASSWORD)
            data = {
                'is_active': True,
                'is_staff': True,
                'is_superuser': True,
                'is_verified': True,
                'password': password,
            }
            User.objects.update_or_create(username=ADMIN_USERNAME, defaults=data)
