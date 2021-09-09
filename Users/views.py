from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .recommendation import get_rec
from . models import Feedback
import pandas as pd

mealPreference = ''

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}! You can now Login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'Users/register.html', {'title': 'Register', 'form': form})


@login_required
def inputPage(request):
    if request.method == 'POST':
        global mealPreference
        mealPreference = request.POST['mealPreference']
        print(mealPreference)
        if request.POST['isVegetarian'] == 'yes':
            return redirect('vegInput')
        elif request.POST['isVegetarian'] == 'no':
            return redirect('nonVegInput')
    return render(request, 'Users/input.html', {'title': 'Input Page'})


@login_required
def veg(request):
    return render(request, 'Users/veg.html', {'title': 'Veg Input'})


@login_required
def nonVeg(request):
    return render(request, 'Users/veg_non-veg.html', {'title': 'Non-Veg Input'})


@login_required
def veg_result(request):
    if mealPreference=='breakfast':                                     #if meal preference is breakfast
        df_veg_breakfast = pd.read_csv('breakfast.csv')
        df_veg_indices_breakfast = pd.read_csv('breakfastindices.csv')
        vegList = request.POST.getlist('vegIngredients')                #User input(stored in list)
        if len(vegList) < 6:
            messages.warning(request, f'You need to select more than 5 ingredients for better recommendation!')
            return redirect('vegInput')
        vegString = " ".join(vegList)                            #list items are converted into string with ' '
        veg_rec_ind = get_rec(vegString, df_veg_breakfast, df_veg_indices_breakfast)   #recommendation algo (returns indices list of recipies)
        recipes = []
        for i in veg_rec_ind:
            recipe = {}
            recipe['name'] = df_veg_breakfast['RecipeName'].iloc[i]
            recipe['ingredients'] = df_veg_breakfast['TranslatedIngredients'].iloc[i]
            recipe['preparation_time'] = df_veg_breakfast['PrepTimeInMins'].iloc[i]
            recipe['cooking_time'] = df_veg_breakfast['CookTimeInMins'].iloc[i]
            recipe['total_time'] = df_veg_breakfast['TotalTimeInMins'].iloc[i]
            recipe['servings'] = df_veg_breakfast['Servings'].iloc[i]
            recipe['cuisine'] = df_veg_breakfast['Cuisine'].iloc[i]
            recipe['instructions'] = df_veg_breakfast['TranslatedInstructions'].iloc[i]
            recipes.append(recipe)                                              #recipes is list of dictionaries

    else:                                                                       #if meal preference is lunch/dinner
        df_veg = pd.read_csv('veg.csv')
        df_veg_indices = pd.read_csv('Veg_indices.csv')
        vegList = request.POST.getlist('vegIngredients')
        if len(vegList) < 6:
            messages.warning(request, f'You need to select more than 5 ingredients for better recommendation!')
            return redirect('vegInput')
        vegString = " ".join(vegList)
        veg_rec_ind = get_rec(vegString, df_veg, df_veg_indices)
        recipes = []
        for i in veg_rec_ind:
            recipe = {}
            recipe['name'] = df_veg['RecipeName'].iloc[i]
            recipe['ingredients'] = df_veg['TranslatedIngredients'].iloc[i]
            recipe['preparation_time'] = df_veg['PrepTimeInMins'].iloc[i]
            recipe['cooking_time'] = df_veg['CookTimeInMins'].iloc[i]
            recipe['total_time'] = df_veg['TotalTimeInMins'].iloc[i]
            recipe['servings'] = df_veg['Servings'].iloc[i]
            recipe['cuisine'] = df_veg['Cuisine'].iloc[i]
            recipe['instructions'] = df_veg['TranslatedInstructions'].iloc[i]
            recipes.append(recipe)

    return render(request, 'Users/veg_result.html', {'title': 'Veg Results Page', 'recipes': recipes, 'mealPreference': mealPreference})


@login_required
def nonveg_result(request):
    if mealPreference=='breakfast':    # breakfast
        df_nonveg_breakfast = pd.read_csv('breakfast.csv')
        df_nonveg_indices_breakfast = pd.read_csv('breakfastindices.csv')
        nonvegList = request.POST.getlist('nonVegIngredients')
        if len(nonvegList) < 6:
            messages.warning(request, f'You need to select more than 5 ingredients for better recommendation!')
            return redirect('nonVegInput')
        nonvegString = " ".join(nonvegList)
        nonveg_rec_ind = get_rec(nonvegString, df_nonveg_breakfast, df_nonveg_indices_breakfast)
        recipes = []
        for i in nonveg_rec_ind:
            recipe = {}
            recipe['name'] = df_nonveg_breakfast['RecipeName'].iloc[i]
            recipe['ingredients'] = df_nonveg_breakfast['TranslatedIngredients'].iloc[i]
            recipe['preparation_time'] = df_nonveg_breakfast['PrepTimeInMins'].iloc[i]
            recipe['cooking_time'] = df_nonveg_breakfast['CookTimeInMins'].iloc[i]
            recipe['total_time'] = df_nonveg_breakfast['TotalTimeInMins'].iloc[i]
            recipe['servings'] = df_nonveg_breakfast['Servings'].iloc[i]
            recipe['cuisine'] = df_nonveg_breakfast['Cuisine'].iloc[i]
            recipe['instructions'] = df_nonveg_breakfast['TranslatedInstructions'].iloc[i]
            recipes.append(recipe)

    else:     #lunch/dinner
        df_nonveg = pd.read_csv('nonveg.csv')
        df_nonveg_indices = pd.read_csv('nonvegindices.csv')
        nonvegList = request.POST.getlist('nonVegIngredients')
        if len(nonvegList) < 6:
            messages.warning(request, f'You need to select more than 5 ingredients for better recommendation!')
            return redirect('nonVegInput')
        nonvegString = " ".join(nonvegList)
        nonveg_rec_ind = get_rec(nonvegString, df_nonveg, df_nonveg_indices)
        recipes = []
        for i in nonveg_rec_ind:
            recipe = {}
            recipe['name'] = df_nonveg['RecipeName'].iloc[i]
            recipe['ingredients'] = df_nonveg['TranslatedIngredients'].iloc[i]
            recipe['preparation_time'] = df_nonveg['PrepTimeInMins'].iloc[i]
            recipe['cooking_time'] = df_nonveg['CookTimeInMins'].iloc[i]
            recipe['total_time'] = df_nonveg['TotalTimeInMins'].iloc[i]
            recipe['servings'] = df_nonveg['Servings'].iloc[i]
            recipe['cuisine'] = df_nonveg['Cuisine'].iloc[i]
            recipe['instructions'] = df_nonveg['TranslatedInstructions'].iloc[i]
            recipes.append(recipe)

    return render(request, 'Users/nonveg_result.html', {'title': 'Non-Veg Results Page', 'recipes': recipes, 'mealPreference': mealPreference})


@login_required
def feedback(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        currentUser = request.user
        userFeedback = Feedback(name=name, email=email, subject=subject, message=message, author=currentUser)
        userFeedback.save()
        messages.success(request, f'Your feedback has been saved successfully!')
        return redirect('feedback')
    return render(request, 'Users/feedback.html', {'title':'Feedback Form'})