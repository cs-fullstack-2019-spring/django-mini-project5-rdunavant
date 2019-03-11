from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('logout/', views.logout, name='logout'),
    path('editRecipe/', views.editRecipe, name="editRecipe"),
    path('allRecipes/', views.allRecipes, name="allRecipes"),
    path('profile/', views.profile, name="profile"),
    path('recipeDetails', views.recipeDetails, name="recipeDetails"),
    path('edit/<int:recipeID>/', views.edit, name="edit"),
    path('delete/<int:recipeID>/', views.delete, name="delete"),
]