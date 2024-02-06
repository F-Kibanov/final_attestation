# Generated by Django 5.0.1 on 2024-02-06 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_cookuser_recipes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cookuser',
            name='recipes',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='author',
            field=models.CharField(default='Неизвестно', max_length=50),
        ),
    ]
