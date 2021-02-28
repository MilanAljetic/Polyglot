# Generated by Django 3.1.7 on 2021-02-28 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0008_auto_20210227_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='users',
            field=models.ManyToManyField(null=True, related_name='names', to='language.User_profile'),
        ),
    ]