# Generated by Django 3.1.7 on 2021-03-06 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0012_remove_group_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='group_post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='language.user_profile'),
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]