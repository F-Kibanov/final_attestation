from django import forms
from django.forms import TimeInput


class AddRecipeForm(forms.Form):
    title = forms.CharField(label='Название блюда',
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Салат "Мимоза"'}))
    description = forms.CharField(label='Описание блюда',
                                  widget=forms.Textarea(
                                      attrs={'class': 'form-control',
                                             'placeholder': 'Классический слоёный салат для праздничного стола.'}))
    ingredients = forms.CharField(label='Необходимые ингредиенты',
                                  widget=forms.Textarea(
                                      attrs={'class': 'form-control',
                                             'placeholder': 'Тунец 200гр.,'
                                                            'Лук 1шт.,'
                                                            'Сыр 100гр.,'
                                                            'Майонез 80гр.,'
                                                            'Яйцо 5шт.,'
                                                            'Укроп 1шт.'}))
    instructions = forms.CharField(label='Способ приготовления',
                                   widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':
                                       '''1. Отварить картофель "в мундире", морковь и яйца. Остудить. Почистить.
                                       2. Все подготовленные составляющие (кроме лука и рыбы) измельчить на средней по размеру ячейке тёрки.
                                       3. Луковицу мелко порубить, залить на 5 минут кипятком, замариновать.
                                       4. Первым слоем выложить половину объёма тертого вареного картофеля. Смазать или сделать сетку из качественного, жирного майонеза.
                                       5. На каждом последующем слое, кроме верхнего, так же сделать сетку или смазывать майонезом.
                                       6. Второй слой – предварительно размятая рыба.
                                       7. Следом мелкорубленный промаринованный лук.
                                       8. Оставшаяся половинка натёртого картофеля.
                                       9. Затем перетёртая морковь.
                                       10. Слой тёртого сыра.
                                       11. Пласт яичного белка.
                                       12. В финале покрыть протёртым прямо на блюдо желтком.'''
                                                                }))
    time_to_cook = forms.TimeField(label='Время приготовления (по желанию)', required=False,
                                   widget=TimeInput(attrs={'class': 'form-control'}))
    author = forms.CharField(label='Автор рецепта', required=False,
                             widget=forms.Textarea(attrs={'class': 'form-control',
                                                          'placeholder': 'Неизвестен'}))

    def __str__(self):
        return self.title


class AddUserForm(forms.Form):
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

    def __str__(self):
        return f'{self.name} {self.surname}'


class ImageForm(forms.Form):
    image = forms.ImageField()
