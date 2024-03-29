from django.db import models
# from multiselectfield import MultiSelectField
from multiselectfield import MultiSelectField

# Add the _get_flatchoices method directly to MultiSelectField
class MultiSelectField(MultiSelectField):
    def _get_flatchoices(self):
        return self.flatchoices

# Create your models here.
class Recipe(models.Model):
    BEGINNER = 'beginner'
    INTERMEDIATE = 'intermediate'
    ADVANCED = 'advanced'
    EXPERIENCE_CHOICES = [
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced'),
            ]

    BREAKFAST = 'breakfast'
    DINNER = 'dinner'
    SNACK = 'snack'
    DESERT = 'dessert'
    MEAL_TYPES= [
            (BREAKFAST, 'Breakfast'),
            (DINNER, 'Dinner'),
            (SNACK, 'Snack'),
            (DESERT, 'Dessert'),   
        ]

    SESAME = 'sesame'
    GLUTEN = 'gluten'
    TREENUTS = 'treenuts'
    PEANUTS = 'peanuts'
    SOY = 'soy'
    WHEAT = 'wheat'
    EGGS = 'eggs'
    SHELLFISH = 'shellfish'
    FISH = 'fish'
    MILK = 'milk'
    NONE_ALLERGEN ='none_allergen'
    ALLERGEN_TYPES = [
        (SESAME, 'Sesame'),
        (GLUTEN, 'Gluten'),
        (TREENUTS, 'Tree Nuts'),
        (PEANUTS, 'Peanuts'),
        (SOY, 'Soy'),
        (WHEAT, 'Wheat'),
        (EGGS, 'Eggs'),
        (SHELLFISH, 'Shellfish'),
        (FISH, 'Fish'),
        (MILK, 'Milk'),
        (NONE_ALLERGEN, 'None'),
    ]

    UNDER30 = 'under30'
    UNDER60 = 'under60'
    OVER60 = 'over60'
    SLOWCOOK = 'slowcook'
    MULTIDAY = 'multiday'
    TIME_TYPES = [
        (UNDER30, 'Under 30 Minutes'),
        (UNDER60, 'Under 60 Minutes'),
        (OVER60, 'Over 60 minutes, less than 3 hours'),
        (SLOWCOOK, 'Slow cooker meal, set it and forget it'),
        (MULTIDAY, 'Can take multiple days to make'),
    ]

    SLOWCOOKER = 'slowcooker'
    INSTANTPOT = 'instantpot'
    HANDMIXER = 'handmixer'
    STANDMIXER = 'standmixer'
    BLENDER = 'blender'
    IMMERSIONBLENDER = 'immersionblender'
    FOODPROCESSOR = 'foodprocessor'
    GRILL = 'grill'
    NONE_EQUIPMENT = 'none-equipment'
    SPECIAL_EQUIPMENT = [
        (SLOWCOOKER, 'Slow Cooker'),
        (INSTANTPOT, 'Pressure Cooker'),
        (HANDMIXER, 'Hand Mixer'),
        (STANDMIXER, 'Stand Mixer'),
        (BLENDER, 'Blender'),
        (IMMERSIONBLENDER, 'Immersion Blender'),
        (FOODPROCESSOR, 'Food Processor'),
        (GRILL, 'Grill'),
        (NONE_EQUIPMENT, 'None')
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    ingredients = models.CharField(max_length=1000, blank=False, null=False)
    experience_level = MultiSelectField(max_length=255, choices=EXPERIENCE_CHOICES, blank=False, null=False, default=BEGINNER)
    meal_type = MultiSelectField(max_length=255, choices=MEAL_TYPES, blank=False, null=False, default=BREAKFAST)
    equipment_needed = MultiSelectField(max_length=255, choices=SPECIAL_EQUIPMENT, blank=False, null=False, default=NONE_EQUIPMENT)
    allergen = MultiSelectField(max_length=255, choices=ALLERGEN_TYPES, blank=False, null=False, default=NONE_ALLERGEN)
    time_commitment = MultiSelectField(max_length=255, choices=TIME_TYPES, blank=False, null=False, default=UNDER30)
    instructions = models.TextField(blank=False, null=False, default="no instructions, sorry")
