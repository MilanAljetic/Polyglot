# Generated by Django 3.1.7 on 2021-02-27 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0005_auto_20210227_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='group_post',
            name='title',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
