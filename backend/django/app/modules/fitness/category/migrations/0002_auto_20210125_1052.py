# Generated by Django 3.0.2 on 2021-01-25 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
