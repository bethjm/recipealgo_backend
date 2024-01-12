from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'name', 'ingredients', 'experience_level', 'meal_type', 'equipment_needed', 'allergen', 'time_commitment', 'instructions')
