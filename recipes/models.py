from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    time_to_cook = models.TimeField(null=True, blank=True, default='Неизвестно')
    author = models.CharField(max_length=50, default='Неизвестно')
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class CookUser(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    register_date = models.DateField(auto_now_add=True)
