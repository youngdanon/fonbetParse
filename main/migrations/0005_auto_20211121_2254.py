# Generated by Django 3.2.9 on 2021-11-21 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_eventsegment_is_live'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventsegment',
            name='score1',
            field=models.IntegerField(default='-1', verbose_name='score1'),
        ),
        migrations.AddField(
            model_name='eventsegment',
            name='score2',
            field=models.IntegerField(default='-1', verbose_name='score2'),
        ),
    ]
