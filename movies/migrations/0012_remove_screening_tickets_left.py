# Generated by Django 4.1.4 on 2022-12-11 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_screening_tickets_left'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='screening',
            name='tickets_left',
        ),
    ]