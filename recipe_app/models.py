from django.db import models
from multiselectfield import MultiSelectField
# from django.core.exceptions import ValidationError

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
    DESERT = 'desert'
    MEAL_TYPES= [
            (BREAKFAST, 'Breakfast'),
            (DINNER, 'Dinner'),
            (SNACK, 'Snack'),
            (DESERT, 'Desert'),   
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
    NONE ='none'
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
        (NONE, 'None')
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
    NONE = 'none'
    SPECIAL_EQUIPMENT = [
        (SLOWCOOKER, 'Slow Cooker'),
        (INSTANTPOT, 'Pressure Cooker'),
        (HANDMIXER, 'Hand Mixer'),
        (STANDMIXER, 'Stand Mixer'),
        (BLENDER, 'Blender'),
        (IMMERSIONBLENDER, 'Immersion Blender'),
        (FOODPROCESSOR, 'Food Processor'),
        (GRILL, 'Grill'),
        (NONE, 'None')
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    ingredients = models.CharField(max_length=1000, blank=False, null=False)
    experience_level = MultiSelectField(max_length=255, choices=EXPERIENCE_CHOICES, blank=False, null=False)
    meal_type = MultiSelectField(max_length=255, choices=MEAL_TYPES, blank=False, null=False)
    equipment_needed = MultiSelectField(max_length=255, choices=SPECIAL_EQUIPMENT, blank=False, null=False)
    allergen = MultiSelectField(max_length=255, choices=ALLERGEN_TYPES, blank=False, null=False)
    time_commitment = MultiSelectField(max_length=255, choices=TIME_TYPES, blank=False, null=False)
    instructions = models.TextField(blank=False, null=False)

    # def clean(self):
    #     super().clean()  # Call the parent clean method
    #     if ',' not in self.ingredients:
    #         raise ValidationError("Please separate each ingredient with commas!")

    def save(self, *args, **kwargs):
        # Convert ingredients to lowercase before saving
        self.ingredients = self.ingredients.lower()

        self.full_clean()  # Ensure validation is triggered before saving
        super().save(*args, **kwargs)