# Generated by Django 4.1.4 on 2022-12-08 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_hall_hall_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='trailer',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
