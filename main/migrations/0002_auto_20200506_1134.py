# Generated by Django 3.0.5 on 2020-05-06 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='trans_1',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='trans_2',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='trans_3',
            field=models.CharField(default='', max_length=100),
        ),
    ]