# Generated by Django 5.1.5 on 2025-02-03 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0018_alter_book_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.IntegerField(verbose_name=30),
        ),
    ]
