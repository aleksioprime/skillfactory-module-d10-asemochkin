# Generated by Django 3.1.6 on 2021-03-14 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=255, verbose_name='Производитель')),
                ('model', models.CharField(max_length=255, verbose_name='Модель')),
                ('year', models.IntegerField(verbose_name='Год выпуска')),
                ('transmission', models.SmallIntegerField(choices=[(1, 'Механика'), (2, 'Автомат'), (3, 'Робот')], default=1)),
                ('color', models.CharField(max_length=255, verbose_name='Цвет')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
                'ordering': ['manufacturer', 'model'],
            },
        ),
    ]
