# Generated by Django 3.2.5 on 2022-03-13 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_auto_20220313_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='is_overdue',
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(blank=True, choices=[('FANTASY', 'Fantasy'), ('SCIENCE FICTION', 'Science Fiction'), ('HORROR', 'Horror'), ('MYSTERY', 'Mystery'), ('ADVENTURE', 'Adventure'), ('REALISTIC FICTION', 'Realistic Fiction'), ('NON-FICTION', 'Non-fiction'), ('HISTORICAL FICTION', 'Historical Fiction')], help_text='Book Genre', max_length=30),
        ),
    ]
