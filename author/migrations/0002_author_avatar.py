# Generated by Django 2.2 on 2022-02-02 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='avatar',
            field=models.ImageField(default='blank', upload_to='images'),
        ),
    ]