from django.shortcuts import render, redirect, get_object_or_404 #pulling redirect
from django.http import HttpResponse #for testing reasons
# Create your views here.
from .forms import RecipeModel
from django.contrib.auth.models import User # Gathers user form from django to add users

def index(request): # for the rendering of index
    recipeList = recipeModel.objects.all() # This gathers all recipes made

# @login_required
def index(request): # for rendering of index
    if request.user.is_authenticated: # makes sure user is logged in
        recipeCollector = recipeModel.objects.get(userIDkey=request.user) # this gets recipe collector
        recipeList = recipeModel.objects.filter(recipeMakeIdKey=recipeCollector) # this gets recipe list that user made

    else:
        recipeList = '' # sets recipelist to empty so no recipes will be shown

    context = \
        {
            'recipeList': recipeList # this add completed recipe list that will later filter out according to logged in user
        }
    return render(request, 'App/index.html', context) # this renders page starting at index

def logout(request):
    return HttpResponse("Welcome")

def editRecipe(request):
    return HttpResponse("Edit recipe")

def allRecipes(request):
    return HttpResponse("All Recipes")

def profile(request):
    return HttpResponse("Profile")

def recipeDetails(request):
    return HttpResponse("Recipe details")

def edit(request, recipeID):
    item = get_object_or_404(RecipeForm, pk=recipeID) #gets the recipe form to be edited
    editForm = RecipeForm(request.POST or None,
                          instance=item) # grabs the form and fills it out with info from the model
    if request.method == 'POST': #makes sure it has retrieved the information before continuing this route
        if editForm.is_valid(): #makes sure that the information entered is valid to requirements
            return redirect('index') # returns to index because you are done
    context = \
    {
        "form": editForm # this gets form to be shown and changed
    }
    return render(request, 'App/editForm.html', context) # renders page for viewing form information to edit

def delete(request, recipeID): #starts down path to delete recipe
    deleteForm = get_object_or_404(RecipeForm, pk = recipeID) # Collects form to delete
    deleteForm.delete() # deletes form when clicking link
    return redirect('index') #returns to index

    if request.method == "POST":
        print(request.POST)
        Recipe.objects.create_recipe(request.POST["picture"], ["name"], ["description"], ["date"], ["creator"], ["edit"])
