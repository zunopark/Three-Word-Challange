# Generated by Django 3.0.5 on 2020-05-03 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200503_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='nickname',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
