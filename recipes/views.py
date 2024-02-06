from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .models import Recipe, CookUser
from .forms import AddRecipeForm, AddUserForm


def index(request):
    random_recipes = Recipe.objects.order_by('?')[:3]
    for recipe in random_recipes:
        recipe.description = f'{" ".join(recipe.description.split()[:5])}...'
    context = {'title': 'Рецепты дня', 'recipes': random_recipes, 'footer': 'Не забудте добавить свой любимый рецепт '
                                                                            'в нашу коллекцию!'}
    return render(request, 'main_page.html', context=context)


def show_all_recipes(request):
    return render(request, 'show_all_recipes.html', context={'title': 'Все рецепты на сайте',
                                                             'recipes': Recipe.objects.all(),
                                                             'footer': 'Надеемся, в нашли для себя что-то новое и '
                                                                       'вкусное =)'})


def show_recipe(request, pk):
    recipe = Recipe.objects.filter(pk=pk).first()
    return render(request, 'show_recipe.html', context={'title': f'Рецепт №{pk}',
                                                        'recipe': recipe,
                                                        'footer': 'Приятного аппетита!'})


def add_recipe(request):
    if request.method == 'POST':
        recipe = AddRecipeForm(request.POST)
        if recipe.is_valid():
            title = recipe.cleaned_data['title']
            description = recipe.cleaned_data['description']
            ingredients = recipe.cleaned_data['ingredients']
            instructions = recipe.cleaned_data['instructions']
            time_to_cook = recipe.cleaned_data['time_to_cook']
            image = recipe.cleaned_data['image']
            if image is not None:
                fs = FileSystemStorage()
                fs.save(image.name, image)
            author = recipe.cleaned_data['author']
            recipe = Recipe(title=title,
                            description=description,
                            ingredients=ingredients,
                            instructions=instructions,
                            time_to_cook=time_to_cook,
                            image=image,
                            author=author,
                            )
            recipe.save()
    else:
        recipe = AddRecipeForm()
    return render(request, 'add_form.html', {'title': 'Добавить новый рецепт', 'form': recipe})


def show_all_users(request):
    return render(request, 'show_all_users.html', context={'title': 'Все пользователи сайта',
                                                           'users': CookUser.objects.all()})


def show_user(request, pk):
    user = CookUser.objects.filter(pk=pk).first()
    return render(request, 'show_user.html', context={'title': f'Пользователь {user.name} {user.surname}',
                                                      'user': user})


def add_user(request):
    if request.method == 'POST':
        user = AddUserForm(request.POST)
        if user.is_valid():
            name = user.cleaned_data['name']
            surname = user.cleaned_data['surname']
            email = user.cleaned_data['email']
            phone = user.cleaned_data['phone']
            # recipes = user.cleaned_data['recipes']
            user = CookUser(name=name,
                            surname=surname,
                            email=email,
                            phone=phone,
                            # recipes=recipes,
                            )
            user.save()
    else:
        user = AddUserForm()
    return render(request, 'add_form.html', {'title': 'Добавить нового пользователя', 'form': user})
