# Generated by Django 2.2.3 on 2021-05-16 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190828_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='remind_on_friday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='remind_on_monday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='remind_on_saturday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='remind_on_sunday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='remind_on_thursday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='remind_on_tuesday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='remind_on_wednesday',
            field=models.BooleanField(default=False),
        ),
    ]