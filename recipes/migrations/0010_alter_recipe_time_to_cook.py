# Generated by Django 5.0.1 on 2024-02-05 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_rename_cook_recipe_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='time_to_cook',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
