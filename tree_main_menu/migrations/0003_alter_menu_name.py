# Generated by Django 5.1 on 2024-08-18 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree_main_menu', '0002_alter_menu_dept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
