# Generated by Django 3.0.2 on 2021-02-04 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20210125_1052'),
        ('exercice', '0012_auto_20210202_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercice',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='exercices_list', to='category.Category'),
        ),
    ]
