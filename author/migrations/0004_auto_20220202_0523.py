# Generated by Django 2.2 on 2022-02-02 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0003_auto_20220202_0522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.IntegerField(default='blank'),
        ),
    ]