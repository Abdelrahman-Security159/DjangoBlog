# Generated by Django 2.2 on 2021-12-15 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('body', models.TextField(max_length=5000)),
                ('auther', models.CharField(max_length=100)),
            ],
        ),
    ]
