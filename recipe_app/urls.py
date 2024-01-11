from django.urls import path
from .views import RecipeListCreateView, RecipeDetailView

urlpatterns = [
    path('api/recipes/', RecipeListCreateView.as_view(), name='recipe_list_create'),
    path('api/recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
]
