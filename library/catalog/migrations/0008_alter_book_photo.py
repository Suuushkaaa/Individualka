# Generated by Django 4.2 on 2025-01-24 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_book_author_alter_book_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='photo',
            field=models.ImageField(help_text='Введите изображение обложки', null=True, upload_to='images', verbose_name='Изображение обложки'),
        ),
    ]
