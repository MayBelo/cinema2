# Generated by Django 4.1.4 on 2022-12-08 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_alter_movie_trailer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='trailer',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
