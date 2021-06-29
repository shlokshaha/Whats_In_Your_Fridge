from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


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
        mealPreference = request.POST['mealPreference']         # ----------------To be handled in result Page-----------------
        print(mealPreference)
        if request.POST['isVegetarian'] == 'yes':
            return redirect('vegInput')
        elif request.POST['isVegetarian'] == 'no':
            return redirect('nonVegInput')
    return render(request, 'Users/input.html',{'title': 'Input Page'})


@login_required
def veg(request):
    return render(request, 'Users/veg.html', {'title': 'Veg Input'})


@login_required
def nonVeg(request):
    return render(request, 'Users/veg_non-veg.html', {'title': 'Non-Veg Input'})