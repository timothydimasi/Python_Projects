# Generated by Django 3.2 on 2021-04-20 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='djangoclasses',
            name='courseNumber',
            field=models.IntegerField(default=0),
        ),
    ]