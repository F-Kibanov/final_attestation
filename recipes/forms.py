import datetime

from django import forms
from django.db.models import DO_NOTHING
from django.forms import TimeInput, RadioSelect
from django.forms.widgets import ChoiceWidget, CheckboxSelectMultiple

from .models import Recipe


class AddRecipeForm(forms.Form):
    title = forms.CharField(label='Название блюда',
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Салат "Мимоза"'}))
    description = forms.CharField(label='Описание блюда',
                                  widget=forms.Textarea(
                                      attrs={'class': 'form-control',
                                             'placeholder': 'Введите краткое описание блюда, '
                                                            'рецепт которого вы предлагаете.'}))
    ingredients = forms.CharField(label='Необходимые ингредиенты',
                                  widget=forms.Textarea(
                                      attrs={'class': 'form-control',
                                             'placeholder': 'Введите список ингредиентов, '
                                                            'необходимых для приготовления '
                                                            'вашего блюда.'}))
    instructions = forms.CharField(label='Способ приготовления',
                                   widget=forms.Textarea(attrs={'class': 'form-control',
                                                                'placeholder': 'Опишите процесс приготовления вашего '
                                                                               'блюда как можно более подробно'}))
    time_to_cook = forms.TimeField(label='Время приготовления (по желанию)', required=False,
                                   widget=TimeInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(label='Изображение готового блюда', required=False)
    author = forms.CharField(label='Автор рецепта', required=False,
                             widget=forms.Textarea(attrs={'class': 'form-control',
                                                          'placeholder': 'Укажите автора рецепта, если знаете... '
                                                                         'Если не знаете - не указывайте!'}))

    # add_date = forms.DateTimeField(initial=datetime.datetime.now)

    def __str__(self):
        return self.title


class AddUserForm(forms.Form):
    # choices = []
    # recipes = Recipe.objects.all()
    # for recipe in recipes:
    #     choices.append(tuple([str(recipe.title[:1]), str(recipe.title)]))
    name = forms.CharField(label='Имя', max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Иван'}))
    surname = forms.CharField(label='Фамилия', max_length=100,
                              widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Иванов'}))
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'user@example.com'}))
    phone = forms.CharField(label='Телефон', max_length=20,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7-999-000-00-00'}))
    # recipes = forms.ChoiceField(label='Ваши рецепты', widget=CheckboxSelectMultiple, choices=choices, required=False)

    # register_date = forms.DateField(initial=datetime.date.today)

    def __str__(self):
        return f'{self.name} {self.surname}'


class ImageForm(forms.Form):
    image = forms.ImageField()
