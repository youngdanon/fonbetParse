# Generated by Django 3.2.9 on 2021-11-21 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20211121_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='score1',
            field=models.IntegerField(default=None, verbose_name='score1'),
        ),
        migrations.AlterField(
            model_name='event',
            name='score2',
            field=models.IntegerField(default=None, verbose_name='score2'),
        ),
        migrations.AlterField(
            model_name='eventsegment',
            name='score1',
            field=models.IntegerField(default=None, verbose_name='score1'),
        ),
        migrations.AlterField(
            model_name='eventsegment',
            name='score2',
            field=models.IntegerField(default=None, verbose_name='score2'),
        ),
    ]
