# Generated by Django 3.0.5 on 2020-05-03 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200503_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='first_translation',
        ),
        migrations.RemoveField(
            model_name='post',
            name='nation',
        ),
        migrations.RemoveField(
            model_name='post',
            name='nickname',
        ),
        migrations.RemoveField(
            model_name='post',
            name='second_translation',
        ),
        migrations.RemoveField(
            model_name='post',
            name='third_translation',
        ),
    ]