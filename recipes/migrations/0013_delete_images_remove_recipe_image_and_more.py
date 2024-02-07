# Generated by Django 5.0.1 on 2024-02-06 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0012_remove_cookuser_recipes_alter_recipe_author'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Images',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='image',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='time_to_cook',
            field=models.TimeField(blank=True, default='Неизвестно', null=True),
        ),
    ]