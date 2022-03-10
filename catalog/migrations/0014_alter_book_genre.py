# Generated by Django 3.2.5 on 2022-02-12 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_alter_book_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(blank=True, choices=[('r', 'Realistic Fiction'), ('R', 'Romance'), ('t', 'Thriller'), ('f', 'Fantasy'), ('m', 'Mystery'), ('n', 'Non-fiction'), ('s', 'Sci-Fi')], help_text='Book Genre', max_length=1),
        ),
    ]