# Generated by Django 5.0.1 on 2024-02-06 00:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_alter_recipe_time_to_cook'),
    ]

    operations = [
        migrations.AddField(
            model_name='cookuser',
            name='recipes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='recipes.recipe'),
        ),
    ]
