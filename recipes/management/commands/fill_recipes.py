import random
import datetime
from django.core.management.base import BaseCommand
from recipes.models import Recipe


class Command(BaseCommand):
    help = 'Create fake recipes'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Recipes generation quantity')

    def handle(self, *args, **kwargs):
        recipes_ = []
        count = kwargs.get('count')
        for i in range(1, count + 1):
            hours = random.randint(0, 2)
            minutes = random.randint(0, 59)
            recipes_.append(Recipe(
                title=f'Название рецепта №{i}, одним своим видом вызывающее аппетит и желание его попробовать',

                description=f'Описание рецепта №{i}, насыщенное подробностями о вкусовых качествах и пользе '
                            f'для здоровья этого блюда',
                ingredients=f'Длинный список интредиентов для приготовления блюда по рецепту №{i}',
                instructions=f'Очень длинное и подробное описание рецепта №{i} со всеми подробностями и '
                             f'тонкостями приготовления, а также рекомендации по напиткам, которые следует '
                             f'подавать с этим блюдом.',
                time_to_cook=datetime.time(hours, minutes),
                # image=f'Изображение блюда №{i}',
                author=f'Повар {i}',
                add_date=datetime.datetime.today,
            ))
        Recipe.objects.bulk_create(recipes_)
