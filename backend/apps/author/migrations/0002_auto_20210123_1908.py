# Generated by Django 3.1.2 on 2021-01-23 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='category',
            field=models.ManyToManyField(blank=True, to='category.Category'),
        ),
    ]
