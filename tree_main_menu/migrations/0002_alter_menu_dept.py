# Generated by Django 5.1 on 2024-08-18 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree_main_menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='dept',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
