# Generated by Django 5.1.5 on 2025-02-03 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0014_remove_book_genre'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Genre',
        ),
    ]
