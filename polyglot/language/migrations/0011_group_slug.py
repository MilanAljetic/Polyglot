# Generated by Django 3.1.7 on 2021-03-06 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0010_group_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='slug',
            field=models.SlugField(allow_unicode=True, null=True, unique=True),
        ),
    ]