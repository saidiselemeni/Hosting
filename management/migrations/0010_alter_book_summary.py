# Generated by Django 5.1.5 on 2025-02-03 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0009_remove_book_genres_remove_reviews_review_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(help_text='Enter a brief description of the book', max_length=1000),
        ),
    ]
