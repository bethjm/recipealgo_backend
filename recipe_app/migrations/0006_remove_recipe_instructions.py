# Generated by Django 5.0.1 on 2024-01-13 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0005_alter_recipe_equipment_needed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='instructions',
        ),
    ]
