from django.urls import path
from . import views

urlpatterns = [
    path('api/recipes/', views.RecipeList.as_view()),
]

