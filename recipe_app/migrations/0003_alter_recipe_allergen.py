# Generated by Django 5.0.1 on 2024-01-12 00:59

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0002_alter_recipe_allergen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='allergen',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('sesame', 'Sesame'), ('gluten', 'Gluten'), ('treenuts', 'Tree Nuts'), ('peanuts', 'Peanuts'), ('soy', 'Soy'), ('wheat', 'Wheat'), ('eggs', 'Eggs'), ('shellfish', 'Shellfish'), ('fish', 'Fish'), ('milk', 'Milk'), ('none', 'None')], max_length=255),
        ),
    ]
