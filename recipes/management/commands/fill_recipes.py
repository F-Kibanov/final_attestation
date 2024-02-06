import random
import datetime
from django.core.management.base import BaseCommand
from recipes.models import CookUser, Recipe


class Command(BaseCommand):
    help = 'Create new recipes'

    def handle(self, *args, **options):
        for i in range(1, 11):
            hours = random.randint(0, 2)
            minutes = random.randint(0, 59)
            recipe = Recipe(title=f'Название рецепта №{i}, одним своим видом вызывающее аппетит и желание '
                                  f'его попробовать',
                            description=f'Описание рецепта №{i}, насыщенное подробностями о вкусовых качествах и пользе '
                                        f'для здоровья этого блюда',
                            ingredients=f'Длинный список интредиентов для приготовления блюда по рецепту №{i}',
                            instructions=f'Очень длинное и подробное описание рецепта №{i} со всеми подробностями и '
                                         f'тонкостями приготовления, а также рекомендации по напиткам, которые следует '
                                         f'подавать с этим блюдом.',
                            time_to_cook=datetime.time(hours, minutes),
                            image=f'Изображение блюда №{i}',
                            author=f'Повар {i}',
                            add_date=datetime.time(),
                            )
            self.stdout.write(self.style.ERROR(f'Рецепт {recipe.title} добавлен!'))
            recipe.save()
