# Generated by Django 3.2.5 on 2022-02-12 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_alter_book_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(blank=True, choices=[('n', 'Non-fiction'), ('r', 'Realistic Fiction'), ('f', 'Fantasy'), ('R', 'Romance'), ('m', 'Mystery'), ('s', 'Sci-Fi'), ('t', 'Thriller')], default='f', help_text='Book Genre', max_length=1),
        ),
    ]
