import random
import datetime
from django.core.management.base import BaseCommand
from recipes.models import CookUser, Recipe


class Command(BaseCommand):
    help = 'Create new users'

    def handle(self, *args, **options):
        for i in range(1, 11):
            # year = random.randint(2000, 2024)
            # month = random.randint(1, 12)
            # day = random.randint(1, 28)
            # recipes_quantity = random.randint(1, 3)
            # random_recipes = Recipe.objects.order_by('?')[:recipes_quantity]
            user = CookUser(name=f'Имя{i}',
                            surname=f'Фамилия{i}',
                            email=f'email{i}@test.com',
                            phone=f'+7-999-{str(i).zfill(7)}',
                            )
            # for recipe in random_recipes:
            #     user.recipes.add(recipe)
            self.stdout.write(self.style.ERROR(f'Пользователь {user.name} {user.surname} добавлен!'))
            user.save()
