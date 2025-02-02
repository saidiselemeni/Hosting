# Generated by Django 5.1.5 on 2025-01-27 08:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_remove_book_genre_book_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(default=1, help_text='Select a genre for this book', on_delete=django.db.models.deletion.CASCADE, to='management.genre'),
        ),
    ]
