from django.core.management.base import BaseCommand
from recipes.models import CookUser, Recipe


class Command(BaseCommand):
    help = 'Create fake users'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Users generation quantity')

    def handle(self, *args, **kwargs):
        users = []
        count = kwargs.get('count')
        for i in range(1, count + 1):
            users.append(CookUser(name=f'Имя{i}',
                                  surname=f'Фамилия{i}',
                                  email=f'email{i}@test.com',
                                  phone=f'+7-999-{str(i).zfill(7)}',
                                  ))
        CookUser.objects.bulk_create(users)
