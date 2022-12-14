# Generated by Django 4.1.3 on 2022-11-17 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall_number', models.IntegerField()),
                ('type', models.SmallIntegerField(choices=[(1, 'Basic'), (2, '3D'), (3, 'VIP')], default=1)),
                ('tickets', models.SmallIntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='movie',
            name='type',
        ),
        migrations.AddField(
            model_name='movie',
            name='age_restrictions',
            field=models.CharField(default='12+', max_length=200),
        ),
        migrations.AddField(
            model_name='movie',
            name='cast',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
