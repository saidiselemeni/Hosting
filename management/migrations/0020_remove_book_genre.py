# Generated by Django 5.1.5 on 2025-02-03 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0019_alter_book_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
    ]
