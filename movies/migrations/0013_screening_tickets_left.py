# Generated by Django 4.1.4 on 2022-12-11 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0012_remove_screening_tickets_left'),
    ]

    operations = [
        migrations.AddField(
            model_name='screening',
            name='tickets_left',
            field=models.SmallIntegerField(default=0),
        ),
    ]
