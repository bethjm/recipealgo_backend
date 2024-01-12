# Generated by Django 5.0.1 on 2024-01-12 01:57

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0003_alter_recipe_allergen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='allergen',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('sesame', 'Sesame'), ('gluten', 'Gluten'), ('treenuts', 'Tree Nuts'), ('peanuts', 'Peanuts'), ('soy', 'Soy'), ('wheat', 'Wheat'), ('eggs', 'Eggs'), ('shellfish', 'Shellfish'), ('fish', 'Fish'), ('milk', 'Milk'), ('none_allergen', 'None')], max_length=255),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='equipment_needed',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('slowcooker', 'Slow Cooker'), ('instantpot', 'Pressure Cooker'), ('handmixer', 'Hand Mixer'), ('standmixer', 'Stand Mixer'), ('blender', 'Blender'), ('immersionblender', 'Immersion Blender'), ('foodprocessor', 'Food Processor'), ('grill', 'Grill'), ('non-equipment', 'None')], max_length=255),
        ),
    ]