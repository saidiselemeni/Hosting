# Generated by Django 5.1.5 on 2025-01-27 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_alter_book_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.TextField(default='any', help_text='Select a genre for this book'),
        ),
    ]
